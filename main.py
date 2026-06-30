import os
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import requests
import urllib.parse
import random
import base64
from datetime import datetime
from PIL import Image, ImageTk
from dotenv import load_dotenv
import shutil

# Get the base path for PyInstaller bundled app
if getattr(sys, 'frozen', False):
    BASE_PATH = sys._MEIPASS
else:
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Load environment variables from .env file
load_dotenv(os.path.join(BASE_PATH, ".env"))

try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
    USE_DND = True
except ImportError:
    USE_DND = False

class UltimateCyborgTool:
    def __init__(self, root):
        self.root = root
        self.root.title("CYBORG NEXUS v3.5")
        self.root.geometry("420x650") 
        self.root.resizable(False, False)
        self.root.attributes('-topmost', True) # ตรึงบนสุดหน้าจอเสมอ
        
        # 📁 โฟลเดอร์เริ่มต้นสำหรับอัปโหลดภาพ
        self.default_image_dir = "/home/boy/รูปภาพ/"
        
        # คุมโทนดีไซน์ไซบอร์กเรืองแสง
        self.bg_dark = "#0A0F14"
        self.bg_panel = "#101820"
        self.neon_blue = "#00F0FF"
        self.neon_red = "#FF0055"
        self.neon_green = "#39FF14"
        self.neon_yellow = "#FFCC00" # สีสำหรับปุ่ม BUG_SCAN
        self.neon_purple = "#BF00FF" # สีสำหรับเอฟเฟคพิเศษ
        self.neon_pink = "#FF00FF" # สีสำหรับการแจ้งเตือน
        self.text_white = "#E2E8F0"
        
        self.root.configure(bg=self.bg_dark)
        self.image_path = None
        # Use writable location for generated outputs
        if getattr(sys, 'frozen', False):
            # When bundled, use user's Documents folder
            output_dir = os.path.join(os.path.expanduser("~"), "Documents", "CYBORG_NEXUS")
        else:
            output_dir = os.path.join(BASE_PATH, "generated_outputs")

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        self.output_dir = output_dir

        # --- [0. HEADER - TOP] ---
        header_frame = tk.Frame(root, bg=self.bg_dark, pady=5, padx=15)
        header_frame.pack(fill=tk.X)
        
        # Control buttons - full width
        btn_frame = tk.Frame(header_frame, bg=self.bg_dark)
        btn_frame.pack(fill=tk.X)
        
        self.upload_btn = tk.Button(btn_frame, text="📥", command=self.upload_image,
                                 font=("Courier New", 9, "bold"), bg="#1A242F", fg=self.neon_blue, relief=tk.FLAT, bd=1)
        self.upload_btn.pack(side=tk.LEFT, padx=1, fill=tk.X, expand=True)
        
        self.save_btn = tk.Button(btn_frame, text="💾", command=self.save_bug_report,
                              font=("Courier New", 9, "bold"), bg="#2A1F3D", fg=self.neon_yellow, relief=tk.FLAT, bd=1)
        self.save_btn.pack(side=tk.LEFT, padx=1, fill=tk.X, expand=True)
        
        self.copy_btn = tk.Button(btn_frame, text="📋", command=self.copy_to_clipboard,
                               font=("Courier New", 9, "bold"), bg="#152836", fg=self.neon_blue, relief=tk.FLAT, bd=1)
        self.copy_btn.pack(side=tk.LEFT, padx=1, fill=tk.X, expand=True)
        
        # Tgpt provider selector
        self.sub_option_var = tk.StringVar(value="sky")
        self.sub_option_combo = ttk.Combobox(btn_frame, textvariable=self.sub_option_var,
                                          font=("Tahoma", 9), width=12)
        self.sub_option_combo["values"] = ["sky", "pollinations", "deepseek", "groq", "ollama"]
        self.sub_option_combo.pack(side=tk.LEFT, padx=2, fill=tk.X, expand=True)
        
        self.exec_btn = tk.Button(btn_frame, text="⚡", command=self.execute_generation, 
                                font=("Courier New", 9, "bold"), bg="#1A2F25", fg=self.neon_green, relief=tk.FLAT, bd=1)
        self.exec_btn.pack(side=tk.LEFT, padx=1, fill=tk.X, expand=True)
        
        self.clean_btn = tk.Button(btn_frame, text="🧹", command=self.clean_output,
                                font=("Courier New", 9, "bold"), bg="#1A2030", fg=self.neon_red, relief=tk.FLAT, bd=1)
        self.clean_btn.pack(side=tk.LEFT, padx=1, fill=tk.X, expand=True)
        
        self.open_folder_btn = tk.Button(btn_frame, text="📤", command=self.open_output_folder,
                               font=("Courier New", 9, "bold"), bg="#1A2435", fg=self.neon_blue, relief=tk.FLAT, bd=1)
        self.open_folder_btn.pack(side=tk.LEFT, padx=1, fill=tk.X, expand=True)

        # Create remaining UI
        # Create remaining UI
        self.create_ui_rest()
        
        # Auto-login on startup (after UI is ready)
        self.root.after(1000, self.do_login)

    def on_provider_select(self):
        """Auto-login when provider is selected"""
        self.do_login()

    def create_ui_rest(self):
        input_frame = tk.LabelFrame(root, text=" [ ENTER_COMMAND_PROMPT ] ", font=("Courier New", 9, "bold"),
                                    fg=self.neon_blue, bg=self.bg_dark, bd=1, relief=tk.SOLID)
        input_frame.pack(fill=tk.X, padx=15, pady=5)
        
        self.cmd_entry = tk.Text(input_frame, font=("Tahoma", 12), bg=self.bg_panel, fg=self.text_white, 
                                  insertbackground=self.neon_blue, bd=0, highlightthickness=1, highlightbackground="#223344", height=5, wrap=tk.WORD)
        self.cmd_entry.pack(fill=tk.X, padx=8, pady=8)

        # --- [3. MODE SELECTOR (เพิ่มตัวเลือก BUG_SCAN)] ---
        mode_frame = tk.Frame(root, bg=self.bg_dark)
        mode_frame.pack(fill=tk.X, padx=15, pady=2)
        
        self.current_mode = tk.StringVar(value="UI_DESIGN")
        
        modes = [
            ("🎨 UI_DESIGN", "UI_DESIGN"), 
            ("💻 CODE", "CODE"), 
            ("🔍 BUG_SCAN", "BUG_SCAN"), # 🆕 เพิ่มฟังก์ชันวิเคราะห์ภาพหาบั๊ก
            ("🖼️ IMAGE", "IMAGE")
        ]
        for text, mode_val in modes:
            rb = tk.Radiobutton(mode_frame, text=text, variable=self.current_mode, value=mode_val,
                                font=("Courier New", 8, "bold"), fg=self.text_white, bg=self.bg_dark,
                                activebackground=self.bg_dark, activeforeground=self.neon_blue,
                                selectcolor=self.bg_panel, indicatoron=0, bd=1, relief=tk.FLAT, padx=4, pady=4)
            rb.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=1)

        # --- [4. DISPLAY & OUTPUT LOG PANEL] ---
        self.display_frame = tk.LabelFrame(root, text=" [ OUTPUT ] ", font=("Courier New", 9, "bold"),
                                           fg=self.neon_blue, bg=self.bg_dark, bd=1, relief=tk.SOLID)
        self.display_frame.pack(fill=tk.X, padx=15, pady=5)
        
        self.log_text = scrolledtext.ScrolledText(self.display_frame, wrap=tk.WORD, font=("Courier New", 10), 
                                                  bg=self.bg_panel, fg=self.text_white, bd=0, height=20)
        self.log_text.pack(fill=tk.X, padx=5, pady=5)
        self.log_text.insert(tk.END, ">> CYBORG READY.\n>> SELECT AI & PRESS LOGIN.\n")
        
        # Enable drag & drop on log_text for BUG_SCAN
        if USE_DND:
            self.log_text.drop_target_register(DND_FILES)
            self.log_text.dnd_bind('<<Drop>>', self.on_drop_image)

        self.img_preview_lbl = tk.Label(self.display_frame, bg=self.bg_panel)

        # --- [5. STATUS BAR] ---
        self.status_bar = tk.Label(root, text="[ WAITING ]", 
                                font=("Courier New", 8, "bold"), fg=self.neon_yellow, bg=self.bg_dark)
        self.status_bar.pack(fill=tk.X, padx=15, pady=2)

        # --- [6. PROGRESS BAR] ---
        self.progress = tk.ttk.Progressbar(
            root, orient=tk.HORIZONTAL, mode='indeterminate'
        )
        self.progress.pack(fill=tk.X, padx=15, pady=(0, 5))
        self.progress.pack_forget()

    def open_output_folder(self):
        """Open output folder in file manager"""
        import subprocess
        try:
            subprocess.run(["xdg-open", self.output_dir])
        except Exception as e:
            messagebox.showinfo("INFO", f"Output folder: {self.output_dir}")
            # Log the error for debugging purposes
            print(f"DEBUG: Failed to open output folder: {e}")

    def clean_output(self):
        """Clear output log"""
        self.log_text.delete(1.0, tk.END)
        self.log_text.insert(tk.END, ">> CLEANED.\n")

    def update_sub_options(self):
        """Update sub options based on selected provider"""
        provider = self.ai_provider.get()
        
        if provider == "ollama":
            self.sub_option_combo.config(values=["llama3", "llama3.2", "mistral", "codellama", "phi3"])
            self.sub_option_var.set("llama3")
            self.api_key_entry.delete(0, tk.END)
            self.api_key_entry.config(state="disabled")
        elif provider == "tgpt":
            self.sub_option_combo.config(values=["sky", "pollinations", "deepseek", "groq", "ollama"])
            self.sub_option_var.set("sky")
            self.api_key_entry.delete(0, tk.END)
            self.api_key_entry.config(state="disabled")
        else:
            self.sub_option_combo.config(values=[])
            self.sub_option_var.set("")
            self.api_key_entry.config(state="normal")
            saved_key = os.environ.get("OPENAI_API_KEY", "")
            if saved_key and saved_key != "sk-your-openai-api-key-here":
                self.api_key_entry.delete(0, tk.END)
                self.api_key_entry.insert(0, saved_key)

    def do_login(self):
        """Login with Tgpt"""
        # Check if UI is ready
        if not hasattr(self, 'log_text') or not self.log_text:
            return
        
        tgpt_provider = self.sub_option_var.get() or "sky"
        self.log_text.insert(tk.END, f"\n>> CHECKING TGPT ({tgpt_provider})...\n")
        self.root.update_idletasks()
        os.environ["AI_PROVIDER"] = "tgpt"
        os.environ["TGPT_PROVIDER"] = tgpt_provider
        
        # Use system tgpt (check if available)
        import platform
        import subprocess
        
        # Check if we're on Windows and provide appropriate guidance
        if platform.system() == "Windows":
            self.log_text.insert(tk.END, f">> INFO: Checking for TGPT installation...\n")
        
        try:
            # Try to use system tgpt (will work if installed via package manager or installer)
            result = subprocess.run(["tgpt", "--version"], capture_output=True, text=True, timeout=5, encoding='utf-8', errors='replace')
            self.log_text.insert(tk.END, f">> TGPT READY! (using system installation)\n")
            return
        except FileNotFoundError:
            self.log_text.insert(tk.END, f">> TGPT NOT FOUND! Please install TGPT first:\n")
            self.log_text.insert(tk.END, f">>   Windows: Use installer from https://github.com/aandrew-me/tgpt\n")
            self.log_text.insert(tk.END, f">>   Or use alternative providers: OpenAI, Google, Ollama, etc.\n")
            self.log_text.insert(tk.END, f">>   After installing TGPT, restart the application.\n")
            return
        except Exception as e:
            # Handle any other errors
            if "WinError 193" in str(e) or "%1 is not a valid Win32 application" in str(e):
                self.log_text.insert(tk.END, f">> ERROR: TGPT compatibility issue. Please reinstall TGPT for Windows.\n")
            else:
                self.log_text.insert(tk.END, f">> ERROR: {str(e)}\n")
            return
        
    def save_bug_report(self):
        """บันทึกผลลัพธ์ลงไฟล์ txt ตามโหมด + วันที่ + เวลา"""
        content = self.log_text.get(1.0, tk.END).strip()
        if not content or len(content) < 5:
            messagebox.showwarning("WARNING", "ยังไม่มีผลลัพธ์!")
            return

        try:
            # สร้างชื่อไฟล์: โหมด_YYYY-MM-DD_HH-MM-SS.txt
            mode = self.current_mode.get() or "OUTPUT"
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{mode}_{timestamp}.txt"
            filepath = os.path.join(self.output_dir, filename)

            # บันทึกลงไฟล์
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

            messagebox.showinfo(
                "SAVED",
                f"บันทึกสำเร็จ!\nไฟล์: {filename}"
            )
            # อัปเดตข้อความปุ่มบันทึก
            original_text = self.save_btn.cget("text")
            self.save_btn.configure(
                text="✅ SAVED!", fg=self.neon_green
            )
            self.root.after(2000, lambda: self.save_btn.configure(
                text=original_text, fg=self.neon_yellow
            ))
        except Exception as e:
            # แสดงข้อความ error ที่เป็นมิตรต่อผู้ใช้
            messagebox.showerror("ERROR", "บันทึกไฟล์ล้มเหลว\nกรุณาลองใหม่อีกครั้ง หรือติดต่อผู้ดูแลระบบ")

    def save_output(self):
        """บันทึกผลลัพธ์ตามโหมดปัจจุบัน"""
        mode = self.current_mode.get()
        content = self.log_text.get(1.0, tk.END).strip()
        
        if not content:
            messagebox.showwarning("WARNING", "ไม่มีเนื้อหาที่จะบันทึก!")
            return
        
        try:
            # สร้างโฟลเดอร์ตามโหมด
            mode_folder = os.path.join(self.output_dir, mode)
            os.makedirs(mode_folder, exist_ok=True)
            
            # สร้างชื่อไฟล์: โหมด_วันที่_เวลา.txt
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{mode}_{timestamp}.txt"
            filepath = os.path.join(mode_folder, filename)
            
            # บันทึกไฟล์
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            
            # อัปเดต last_mode
            self.last_mode = mode
            
            # แสดงข้อความสำเร็จ
            messagebox.showinfo(
                "SAVED",
                f"บันทึกสำเร็จ!\nโฟลเดอร์: {mode_folder}\nไฟล์: {filename}"
            )
            
            # อัปเดตปุ่ม
            original_text = self.save_btn.cget("text")
            self.save_btn.configure(text="✅ SAVED!", fg=self.neon_green)
            self.root.after(2000, lambda: self.save_btn.configure(
                text=original_text, fg=self.neon_yellow
            ))
            
            # เปิดโฟลเดอร์
            self.open_folder(mode_folder)
            
        except Exception as e:
            messagebox.showerror("ERROR", f"บันทึกไฟล์ล้มเหลว: {str(e)}")

    def copy_to_clipboard(self):
        content = self.log_text.get(1.0, tk.END).strip()
        if content and not content.startswith(">> CYBORG ENGINE V3.5"):
            self.root.clipboard_clear()
            self.root.clipboard_append(content)
            self.root.update()
            
            original_text = self.copy_btn.cget("text")
            self.copy_btn.configure(text="✅ COPIED TO CLIPBOARD!", fg=self.neon_green)
            self.root.after(1500, lambda: self.copy_btn.configure(text=original_text, fg=self.neon_blue))
        else:
            messagebox.showwarning("EMPTY", "ไม่มีข้อมูลข้อความให้คัดลอก!")

    def upload_image(self):
        # ใช้โฟลเดอร์เริ่มต้นที่ตั้งค่าไว้
        initial_dir = self.default_image_dir if os.path.exists(self.default_image_dir) else "/"
        file_path = filedialog.askopenfilename(
            initialdir=initial_dir,
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.webp")]
        )
        if file_path:
            self.image_path = file_path
            # แสดงพรีวิวภาพขนาดเล็กในกล่อง Log
            self.log_text.pack_forget() 
            img = Image.open(file_path)
            img.thumbnail((360, 250))
            img_tk = ImageTk.PhotoImage(img)
            self.img_preview_lbl.configure(image=img_tk)
            self.img_preview_lbl.image = img_tk
            self.img_preview_lbl.pack(fill=tk.BOTH, expand=True, pady=10)
            
            # สลับหน้าโหมดไป BUG_SCAN ให้อัตโนมัติเพื่อความสะดวก
            self.current_mode.set("BUG_SCAN")
            messagebox.showinfo("SUCCESS", f"โหลดรูปภาพสำเร็จ! พร้อมเข้าสู่โหมด BUG_SCAN\nไฟล์: {os.path.basename(file_path)}")

    def on_drop_image(self, event):
        """Handle dropped image file"""
        if event.data:
            # Get file path from drop event
            file_path = event.data
            if file_path.startswith('{') and file_path.endswith('}'):
                file_path = file_path[1:-1]
            file_path = file_path.strip()
            
            if os.path.exists(file_path) and file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                self.image_path = file_path
                self.log_text.pack_forget()
                img = Image.open(file_path)
                img.thumbnail((360, 250))
                img_tk = ImageTk.PhotoImage(img)
                self.img_preview_lbl.configure(image=img_tk)
                self.img_preview_lbl.image = img_tk
                self.img_preview_lbl.pack(fill=tk.BOTH, expand=True, pady=10)
                self.current_mode.set("BUG_SCAN")
                self.log_text.insert(tk.END, f"\n>> DROPPED: {os.path.basename(file_path)}\n>> MODE: BUG_SCAN\n")
            else:
                messagebox.showwarning("WARNING", "กรุณาลากไฟล์ภาพ (png, jpg, jpeg, webp)")

    def execute_generation(self):
        prompt = self.cmd_entry.get("1.0", tk.END).strip()
        mode = self.current_mode.get()
        
        self.log_text.pack(fill=tk.BOTH, expand=True)
        self.img_preview_lbl.pack_forget()
        self.log_text.delete(1.0, tk.END)
        
        if mode == "BUG_SCAN":
            if not self.image_path:
                messagebox.showwarning("WARNING", "กรุณากดปุ่ม UPLOAD SCREENSHOT เพื่อเลือกภาพหน้าจอบั๊กก่อน!")
                return
            self.call_worker_vision_api()
        elif mode == "UI_DESIGN":
            if not prompt or prompt.startswith("เช่น"):
                messagebox.showwarning("WARNING", "กรุณากรอกคำสั่งบรีฟงานด้วย!")
                return
            self.call_worker_api(prompt, is_design=True)
        elif mode == "CODE":
            if not prompt or prompt.startswith("เช่น"):
                messagebox.showwarning("WARNING", "กรุณากรอกคำสั่งบรีฟงานด้วย!")
                return
            self.call_worker_api(prompt, is_design=False)
        elif mode == "IMAGE":
            if not prompt or prompt.startswith("เช่น"):
                messagebox.showwarning("WARNING", "กรุณากรอกคำสั่งบรีฟงานด้วย!")
                return
            self.generate_image_tool(prompt)

    # 📡 🆕 ฟังก์ชันส่งภาพ + คำสั่งคุยกับระบบ Vision ผ่านเซิร์ฟเวอร์คนกลาง
    def call_worker_vision_api(self):
        self.show_progress(True)
        self.log_text.insert(tk.END, f">> TARGET_FILE: {os.path.basename(self.image_path)}\n>> DECODING IMAGE TO BASE64 BYTES...\n>> CONNECTING VISION TUNNEL TO WORKER SERVER...\n\n")
        self.root.update_idletasks()

        try:
            # 1. แปลงไฟล์ภาพท้องถิ่นให้เป็นสตริง Base64 เพื่อแพ็ครวมใน JSON ได้
            with open(self.image_path, "rb") as img_file:
                base64_image = base64.b64encode(img_file.read()).decode('utf-8')

            # 2. เตรียมคำสั่งวิเคราะห์เฉพาะเจาะจง
            user_msg = (
                "ช่วยตรวจหาข้อผิดพลาดจากภาพ UI นี้ แล้วอธิบายตำแหน่งและลักษณะความผิดพลาด "
                "พร้อมคำแนะนำการแก้ไข (ตอบเป็นภาษาไทย)\n\n"
                "=== รูปแบบผลลัพธ์ที่ต้องการ ===\n"
                "🐛 ปัญหาที่พบ:\n"
                "[รายการปัญหาที่ค้นพบ]\n\n"
                "🔧 วิธีแก้ไข:\n"
                "ข้อ 1: [วิธีแก้ปัญหาที่ 1]\n"
                "ข้อ 2: [วิธีแก้ปัญหาที่ 2]\n"
                "[เพิ่มเติมได้ตามจำเป็น]"
            )
            if self.cmd_entry.get("1.0", tk.END).strip() and not self.cmd_entry.get("1.0", tk.END).strip().startswith("เช่น"):
                user_msg += f"\n(ข้อมูลเพิ่มเติมจากผู้ใช้: {self.cmd_entry.get('1.0', tk.END).strip()})"

            headers = {"Content-Type": "application/json"}

            # 3. โครงสร้าง Payload รูปแบบ Multimodal (ส่งได้ทั้งข้อความและภาพ)
            provider = os.environ.get("AI_PROVIDER", "openai")
            api_key = os.environ.get("OPENAI_API_KEY", "")
            
            if provider == "ollama":
                self.log_text.insert(tk.END, f">> VISION NOT SUPPORTED FOR OLLAMA\n>> Please use OpenAI or Google for Vision\n")
                self.show_progress(False)
                return
            
            if provider == "tgpt":
                # Use Gemini vision API for image analysis
                self.log_text.insert(tk.END, f">> USING GEMINI VISION...\n")
                self.root.update_idletasks()
                import requests
                import base64 as base64_module
                gemini_key = os.environ.get("GEMINI_API_KEY", "")
                if not gemini_key:
                    self.log_text.insert(tk.END, ">> ERROR: GEMINI_API_KEY not set\n")
                    self.show_progress(False)
                    return
                try:
                    # Encode image to base64
                    with open(self.image_path, "rb") as f:
                        img_b64 = base64_module.b64encode(f.read()).decode()
                    
                    # Use Gemini 2.5 Flash vision API
                    api_url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={gemini_key}"
                    headers = {"Content-Type": "application/json"}
                    payload = {
                        "contents": [{
                            "parts": [
                                {"text": user_msg},
                                {"inlineData": {"mimeType": "image/png", "data": img_b64}}
                            ]
                        }]
                    }
                    res = requests.post(api_url, json=payload, headers=headers, timeout=90)
                    if res.status_code == 200:
                        result = res.json()["candidates"][0]["content"]["parts"][0]["text"]
                        self.log_text.insert(tk.END, ">> ANALYSIS COMPLETE:\n\n" + result)
                    else:
                        self.log_text.insert(tk.END, f">> ERROR: {res.text[:200]}")
                except Exception as e:
                    self.log_text.insert(tk.END, f">> ERROR: {str(e)}")
                self.show_progress(False)
                return
            
            if provider == "openai":
                headers["Authorization"] = f"Bearer {api_key}"
                payload = {
                    "model": "gpt-4o-mini",
                    "messages": [
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": user_msg},
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:image/jpeg;base64,{base64_image}"
                                    }
                                }
                            ]
                        }
                    ]
                }
                response = requests.post(
                    "https://api.openai.com/v1/chat/completions",
                    json=payload, headers=headers, timeout=90
                )
            elif provider == "google":
                headers["x-goog-api-key"] = api_key
                payload = {
                    "contents": [
                        {
                            "parts": [
                                {"text": user_msg},
                                {"inline_data": {"mime_type": "image/jpeg", "data": base64_image}}
                            ]
                        }
                    ]
                }
                response = requests.post(
                    f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key={api_key}",
                    json=payload, headers=headers, timeout=90
                )
            else:
                self.log_text.insert(tk.END, f">> VISION NOT SUPPORTED FOR {provider.upper()}\n>> Please use OpenAI or Google for Vision\n")
                self.show_progress(False)
                return
            if response.status_code == 200:
                data = response.json()
                if provider == "google":
                    ai_response = data["candidates"][0]["content"]["parts"][0]["text"]
                else:
                    ai_response = data["choices"][0]["message"]["content"]
                # จัดรูปแบบผลลัพธ์ให้อ่านง่าย
                formatted_response = self.format_bug_response(ai_response)
                self.log_text.insert(
                    tk.END, ">> DECRYPTION COMPLETE. BUG REPORTED:\n\n" + formatted_response
                )
            else:
                self.log_text.insert(
                    tk.END,
                    f">> SERVER_ERROR: HTTP {response.status_code}\n>> {response.text[:300]}",
                )
        except Exception as e:
            self.log_text.insert(tk.END, f">> VISION_GATEWAY_ERROR: {str(e)}")
        finally:
            self.show_progress(False)

    def format_bug_response(self, text):
        """จัดรูปแบบผลลัพธ์ BUG ให้อ่านง่าย"""
        # เพิ่มการเน้นประเภทข้อบกพร่อง
        formatted = text

        # เพิ่มไอเซ็มโคนสำหรับส่วนสำคัญ
        replacements = [
            ("ปัญหาที่พบ", "🐛 ปัญหาที่พบ:"),
            ("วิธีแก้ไข", "🔧 วิธีแก้ไข:"),
            ("ข้อ 1", "🔹 ข้อ 1"),
            ("ข้อ 2", "🔹 ข้อ 2"),
            ("ข้อ 3", "🔹 ข้อ 3"),
            ("ข้อ 4", "🔹 ข้อ 4"),
            ("Error", "❌ Error"),
            ("Warning", "⚠️ Warning"),
            ("Overflow", "📏 Overflow"),
        ]

        for old, new in replacements:
            formatted = formatted.replace(old, new)

        return formatted

    def show_progress(self, show=True, message="AI กำลังคิด วิเคราะห์ ประมวลผล..."):
        """แสดง/ซ่อน Progress Bar ขณะรอผลลัพธ์"""
        if show:
            self.progress.pack(fill=tk.X, padx=15, pady=(0, 5))
            self.progress.start(10)
            self.status_bar.configure(text=message, fg=self.neon_yellow)
            self.exec_btn.configure(state=tk.DISABLED)
        else:
            self.progress.stop()
            self.progress.pack_forget()
            self.status_bar.configure(text="[ พร้อม ]", fg=self.neon_green)
            self.exec_btn.configure(state=tk.NORMAL)

    def call_worker_api(self, prompt, is_design=True):
        provider = os.environ.get("AI_PROVIDER", "openai")
        api_key = os.environ.get("OPENAI_API_KEY", "")
        
        if not api_key and provider not in ["ollama", "tgpt"]:
            messagebox.showwarning("WARNING", "กรุณา LOGIN ก่อน!")
            return
        
        self.log_text.insert(tk.END, f">> CONNECTING TO {provider.upper()} AI...\n\n")
        self.root.update_idletasks()

        if is_design:
            system_prompt = (
                "คุณคือ UI/UX Architect จงออกแบบระบบดีไซน์ครบวงจร: "
                "1. BRAND IDENTITY, 2. SVG ICONS CODE, 3. UI/UX CORE CODE, "
                "4. CSS ANIMATIONS ตอบเป็นภาษาไทย"
            )
        else:
            system_prompt = (
                "คุณคือ Software Architect จงเขียนโค้ดตัวอย่างที่สะอาด "
                "และอธิบายสั้นๆ"
            )

        try:
            self.show_progress(True)
            headers = {"Content-Type": "application/json"}
            
            if provider == "openai":
                headers["Authorization"] = f"Bearer {api_key}"
                res = requests.post(
                    "https://api.openai.com/v1/chat/completions",
                    json={
                        "model": "gpt-4o-mini",
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": prompt},
                        ],
                    },
                    headers=headers,
                    timeout=60,
                )
                if res.status_code == 200:
                    self.log_text.insert(tk.END, res.json()["choices"][0]["message"]["content"])
                    if is_design:
                        self.root.after(100, lambda: self.generate_ui_mockup_bg(prompt))
                else:
                    self.log_text.insert(tk.END, f">> ERROR: {res.text[:300]}")
                    
            elif provider == "google":
                headers["x-goog-api-key"] = api_key
                res = requests.post(
                    "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key=" + api_key,
                    json={
                        "contents": [{"parts": [{"text": f"{system_prompt}\n\n{prompt}"}]}]
                    },
                    headers=headers,
                    timeout=60,
                )
                if res.status_code == 200:
                    self.log_text.insert(tk.END, res.json()["candidates"][0]["content"]["parts"][0]["text"])
                    if is_design:
                        self.root.after(100, lambda: self.generate_ui_mockup_bg(prompt))
                else:
                    self.log_text.insert(tk.END, f">> ERROR: {res.text[:300]}")
                    
            elif provider == "meta":
                headers["Authorization"] = f"Bearer {api_key}"
                res = requests.post(
                    "https://api.meta.com/v1/chat/completions",
                    json={
                        "model": "llama-3.2-90b",
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": prompt},
                        ],
                    },
                    headers=headers,
                    timeout=60,
                )
                if res.status_code == 200:
                    self.log_text.insert(tk.END, res.json()["choices"][0]["message"]["content"])
                else:
                    self.log_text.insert(tk.END, f">> ERROR: {res.text[:300]}")
                    
            elif provider == "ollama":
                model = os.environ.get("OLLAMA_MODEL", "llama3")
                res = requests.post(
                    "http://localhost:11434/api/chat",
                    json={
                        "model": model,
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": prompt},
                        ],
                    },
                    timeout=60,
                )
                if res.status_code == 200:
                    self.log_text.insert(tk.END, res.json()["message"]["content"])
                else:
                    self.log_text.insert(tk.END, f">> ERROR: {res.text[:300]}")
                    
            elif provider == "tgpt":
                # Check if we're on Windows and provide appropriate guidance
                import platform
                import subprocess
                
                if platform.system() == "Windows":
                    self.log_text.insert(tk.END, f">> INFO: Checking for TGPT installation...\n")
                
                tgpt_provider = os.environ.get("TGPT_PROVIDER", "sky")
                full_prompt = f"{system_prompt}\n\n{prompt}"
                try:
                    # Try to use system tgpt (will work if installed via package manager or installer)
                    result = subprocess.run(
                        ["tgpt", "-q", "--provider", tgpt_provider, full_prompt],
                        capture_output=True, text=True, timeout=60, encoding='utf-8', errors='replace'
                    )
                    self.log_text.insert(tk.END, result.stdout)
                except FileNotFoundError:
                    self.log_text.insert(tk.END, f">> TGPT NOT FOUND! Please install TGPT first:\n")
                    self.log_text.insert(tk.END, f">>   Windows: Use installer from https://github.com/aandrew-me/tgpt\n")
                    self.log_text.insert(tk.END, f">>   Or use alternative providers: OpenAI, Google, Ollama, etc.\n")
                    self.log_text.insert(tk.END, f">>   After installing TGPT, restart the application.")
                except subprocess.TimeoutExpired:
                    self.log_text.insert(tk.END, f">> ERROR: TIMEOUT")
                except Exception as e:
                    # Handle any other errors
                    if "WinError 193" in str(e) or "%1 is not a valid Win32 application" in str(e):
                        self.log_text.insert(tk.END, f">> ERROR: TGPT compatibility issue. Please reinstall TGPT for Windows.")
                    else:
                        self.log_text.insert(tk.END, f">> ERROR: {str(e)}")
                    
        except Exception as e:
            self.log_text.insert(tk.END, f">> ERROR: {str(e)}")
        finally:
            self.show_progress(False)

    def generate_ui_mockup_bg(self, prompt):
        try:
            self.show_progress(True)
            res = requests.get(
                f"https://pollinations.ai/{urllib.parse.quote(prompt)}"
                f"?width=512&height=512&model=flux&nologo=true",
                stream=True,
            )
            if res.status_code == 200:
                filepath = os.path.join(
                    self.output_dir,
                    f"ui_preview_{random.randint(100, 999)}.png",
                )
                with open(filepath, "wb") as f:
                    for chunk in res.iter_content(chunk_size=8192):
                        f.write(chunk)
                self.log_text.insert(
                    tk.END, f"\n\n>> [VISUAL MOCKUP GENERATED] >> SAVED AT: {filepath}"
                )
        except Exception:
            pass
        finally:
            self.show_progress(False)

    def generate_image_tool(self, prompt):
        provider = os.environ.get("AI_PROVIDER", "openai")
        
        try:
            self.show_progress(True)
            
            # Use tgpt for image generation
            if provider == "tgpt":
                self.log_text.insert(tk.END, f">> GENERATING IMAGE WITH TGPT...")
                self.root.update_idletasks()
                import subprocess
                tgpt_path = os.path.join(BASE_PATH, "tgpt")
                filepath = os.path.join(self.output_dir, f"art_{random.randint(100, 999)}.png")
                try:
                    subprocess.run(
                        [tgpt_path, "-q", "--img", "--out", filepath, "--height", "512", "--width", "512", prompt],
                        capture_output=True, text=True, timeout=60
                    )
                    if os.path.exists(filepath):
                        self.log_text.pack_forget()
                        img = Image.open(filepath)
                        img.thumbnail((360, 360))
                        img_tk = ImageTk.PhotoImage(img)
                        self.img_preview_lbl.configure(image=img_tk)
                        self.img_preview_lbl.image = img_tk
                        self.img_preview_lbl.pack(fill=tk.BOTH, expand=True, pady=10)
                        self.log_text.delete(1.0, tk.END)
                        self.log_text.insert(tk.END, f">> IMAGE GENERATED.\n>> PATH: {filepath}")
                    else:
                        self.log_text.insert(tk.END, f">> ERROR: Image not generated")
                except Exception as e:
                    self.log_text.insert(tk.END, f">> ERROR: {str(e)}")
                self.show_progress(False)
                return
            
            self.log_text.insert(tk.END, f">> DOWNLOADING ASSET FROM IMAGE CORE...")
            self.root.update_idletasks()
            res = requests.get(
                f"https://pollinations.ai/{urllib.parse.quote(prompt)}"
                f"?width=512&height=512&model=flux&nologo=true",
                stream=True,
            )
            if res.status_code == 200:
                filepath = os.path.join(
                    self.output_dir, f"art_{random.randint(100, 999)}.png"
                )
                with open(filepath, "wb") as f:
                    for chunk in res.iter_content(chunk_size=8192):
                        f.write(chunk)
                self.log_text.pack_forget()
                img = Image.open(filepath)
                img.thumbnail((360, 360))
                img_tk = ImageTk.PhotoImage(img)
                self.img_preview_lbl.configure(image=img_tk)
                self.img_preview_lbl.image = img_tk
                self.img_preview_lbl.pack(fill=tk.BOTH, expand=True, pady=10)
                self.log_text.delete(1.0, tk.END)
                self.log_text.insert(
                    tk.END, f">> IMAGE GENERATED.\n>> PATH: {filepath}"
                )
        except Exception as e:
            self.log_text.insert(tk.END, f"\n>> ERROR: {str(e)}")
        finally:
            self.show_progress(False)


if __name__ == "__main__":
    if USE_DND:
        root = TkinterDnD.Tk()
    else:
        root = tk.Tk()
    app = UltimateCyborgTool(root)
    root.mainloop()
