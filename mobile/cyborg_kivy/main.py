import os
import sys
import base64
import requests
from datetime import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.filechooser import FileChooserIconView
from kivy.clock import Clock
from kivy.utils import platform
from kivy.core.window import Window

# Load KV file
Builder.load_file('cyborg.kv')

# Colors
BG_DARK = (0.04, 0.06, 0.08, 1)
NEON_BLUE = (0, 1, 1, 1)
NEON_GREEN = (0, 0.8, 0.1, 1)
NEON_YELLOW = (1, 0.8, 0, 1)


class BugScanScreen(Screen):
    camera_active = False
    captured = False
    camera_height = 0.4
    preview_path = ''
    log_text = '>> พร้อมถ่ายภาพ / เลือกรูป...\n'
    header_text = '[b]🔍 BUG_SCAN MODE[/b]'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.captured_image_path = None
        self.camera_index = 0
        Clock.schedule_once(self.init_camera, 0.1)
    
    def init_camera(self, dt):
        """Initialize camera on Android"""
        if platform == 'android':
            try:
                from android.permissions import request_permissions, Permission
                request_permissions([Permission.CAMERA])
            except:
                pass
    
    def toggle_camera(self):
        """เปิด/ปิดกล้อง"""
        self.camera_active = not self.camera_active
        if hasattr(self.ids, 'camera_widget'):
            self.ids.camera_widget.play = self.camera_active
            self.ids.camera_widget.opacity = 1 if self.camera_active else 0
    
    def capture_photo(self):
        """ถ่ายภาพจากกล้อง"""
        if not self.camera_active:
            self.header_text = '[b]📸 กดเปิดกล้องก่อน[/b]'
            return
            
        camera = self.ids.camera_widget
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"bug_scan_{timestamp}.png"
        filepath = os.path.join(self.get_output_dir(), filename)
        
        try:
            camera.export_to_png(filepath)
            self.captured_image_path = filepath
            self.captured = True
            self.preview_path = filepath
            self.log_text += f"\n>> ถ่ายภาพสำเร็จ: {filename}\n>> แตะ 'วิเคราะห์ภาพ' เพื่อเริ่มการวิเคราะห์\n"
            self.header_text = '[b]✅ ถ่ายภาพแล้ว - แตะวิเคราะห์[/b]'
            
        except Exception as e:
            self.log_text += f"\n>> เกิดข้อผิดพลาด: {str(e)}\n"
            self.captured = False
    
    def open_file_chooser(self):
        """เปิดตัวเลือกไฟล์"""
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        filechooser = FileChooserIconView(filters=['*.png', '*.jpg', '*.jpeg', '*.webp'])
        content.add_widget(filechooser)
        
        btn_layout = BoxLayout(size_hint_y=None, height=40, spacing=10)
        btn_ok = Button(text='✅ เลือก', size_hint_x=None, width=100)
        btn_cancel = Button(text='❌ ยกเลิก', size_hint_x=None, width=100)
        
        btn_layout.add_widget(btn_ok)
        btn_layout.add_widget(btn_cancel)
        content.add_widget(btn_layout)
        
        popup = Popup(title='📂 เลือกภาพสำหรับวิเคราะห์', 
                     content=content, 
                     size_hint=(0.95, 0.9),
                     background_color=BG_DARK)
        
        btn_ok.bind(on_press=lambda x: self.select_image(filechooser.selection, popup))
        btn_cancel.bind(on_press=popup.dismiss)
        popup.open()
    
    def select_image(self, selection, popup):
        """เลือกภาพจากแกเลอรี่"""
        if selection:
            filepath = selection[0]
            self.captured_image_path = filepath
            self.preview_path = filepath
            self.captured = True
            self.header_text = f'[b]📷 {os.path.basename(filepath)}[/b]'
            self.log_text += f"\n>> เลือกรูป: {os.path.basename(filepath)}\n>> แตะ 'วิเคราะห์ภาพ' เพื่อเริ่มการวิเคราะห์\n"
        popup.dismiss()
    
    def analyze_captured_image(self):
        """วิเคราะห์ภาพที่ถ่าย/เลือก"""
        if not self.captured_image_path:
            self.log_text += "\n>> ยังไม่มีภาพที่ถ่ายหรือเลือก\n"
            return
        
        self.log_text += "\n>> กำลังวิเคราะห์...\n"
        self.analyze_bug_image(self.captured_image_path)
    
    def analyze_bug_image(self, image_path):
        """ส่งภาพไปวิเคราะห์ผ่าน Vision API"""
        try:
            with open(image_path, "rb") as f:
                base64_image = base64.b64encode(f.read()).decode('utf-8')
            
            user_msg = (
                "ช่วยตรวจหาข้อผิดพลาดจากภาพ UI นี้ แล้วอธิบายตำแหน่งและลักษณะความผิดพลาด "
                "พร้อมคำแนะนำการแก้ไข (ตอบเป็นภาษาไทย)\n\n"
                "=== รูปแบบผลลัพธ์ที่ต้องการ ===\n"
                "🐛 ปัญหาที่พบ:\n"
                "[รายการปัญหาที่ค้นพบ]\n\n"
                "🔧 วิธีแก้ไข:\n"
                "ข้อ 1: [วิธีแก้ปัญหาที่ 1]\n"
                "ข้อ 2: [วิธีแก้ปัญหาที่ 2]"
            )
            
            # ใช้ Gemini Vision API
            gemini_key = os.environ.get("GEMINI_API_KEY", "")
            if not gemini_key:
                self.log_text += "\n>> ⚠️ ไม่พบ GEMINI_API_KEY\n>> กรุณาตั้งค่าใน Settings\n"
                return
            
            api_url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={gemini_key}"
            headers = {"Content-Type": "application/json"}
            payload = {
                "contents": [{
                    "parts": [
                        {"text": user_msg},
                        {"inlineData": {"mimeType": "image/png", "data": base64_image}}
                    ]
                }]
            }
            
            res = requests.post(api_url, json=payload, headers=headers, timeout=90)
            if res.status_code == 200:
                result = res.json()["candidates"][0]["content"]["parts"][0]["text"]
                formatted = self.format_bug_response(result)
                self.log_text += "\n🎯 ผลการวิเคราะห์:\n\n" + formatted
                self.header_text = '[b]✅ วิเคราะห์เสร็จ[/b]'
            else:
                self.log_text += f"\n>> ERROR: {res.text[:200]}\n"
                
        except Exception as e:
            self.log_text += f"\n>> ERROR: {str(e)}\n"
    
    def format_bug_response(self, text):
        """จัดรูปแบบผลลัพธ์ BUG"""
        formatted = text
        replacements = [
            ("ปัญหาที่พบ", "🐛 ปัญหาที่พบ:"),
            ("วิธีแก้ไข", "🔧 วิธีแก้ไข:"),
            ("ข้อ 1", "🔹 ข้อ 1"),
            ("ข้อ 2", "🔹 ข้อ 2"),
            ("ข้อ 3", "🔹 ข้อ 3"),
            ("ข้อ 4", "🔹 ข้อ 4"),
            ("Error", "❌ Error"),
            ("Warning", "⚠️ Warning"),
        ]
        for old, new in replacements:
            formatted = formatted.replace(old, new)
        return formatted
    
    def get_output_dir(self):
        """ไดเรกทอรีสำหรับบันทึกไฟล์"""
        if platform == 'android':
            try:
                from android.storage import app_storage_path
                return app_storage_path()
            except:
                return '/storage/emulated/0/Download'
        else:
            return os.path.join(os.path.dirname(__file__), 'output')


class MainScreen(Screen):
    current_mode = 'UI_DESIGN'
    output_text = '>> CYBORG NEXUS Mobile v1.0\n>> เลือกโหมดเพื่อเริ่มต้น\n'
    
    def switch_mode(self, mode):
        self.current_mode = mode
        self.output_text += f'\n>> 🔄 เปลี่ยนโหมดเป็น: {mode}\n'
        # ถ้าเป็น BUG_SCAN ให้ไปที่หน้าจอกล้อง
        if mode == 'BUG_SCAN':
            self.manager.current = 'bug_scan'
    
    def set_provider(self, provider):
        os.environ["TGPT_PROVIDER"] = provider
        self.output_text += f'\n>> 🔧 ตั้งค่า Provider: {provider}\n'
    
    def execute_command(self):
        cmd = self.ids.cmd_input.text
        self.output_text += f'\n>> ⚡ กำลังประมวลผล ({self.current_mode})...\n'
        # TODO: Implement API call
    
    def save_output(self):
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"output_{timestamp}.txt"
            filepath = os.path.join(os.path.dirname(__file__), 'output', filename)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(self.output_text)
            self.output_text += f'\n>> 💾 บันทึกแล้ว: {filename}\n'
        except Exception as e:
            self.output_text += f'\n>> บันทึกล้มเหลว: {str(e)}\n'


class CyborgKivyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(BugScanScreen(name='bug_scan'))
        return sm
    
    def on_start(self):
        self.title = 'CYBORG NEXUS Mobile'
        
        # Request Android permissions
        if platform == 'android':
            try:
                from android.permissions import request_permissions, Permission
                request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE])
            except:
                pass


if __name__ == '__main__':
    CyborgKivyApp().run()