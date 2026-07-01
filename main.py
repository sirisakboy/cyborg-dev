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

class LoginWindow:
    """หน้าต่างล็อคอินของ CYBORG NEXUS"""
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 CYBORG NEXUS - LOGIN")
        self.root.geometry("460x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#0A0F14")
        
        # สีสำหรับดีไซน์
        self.bg_dark = "#0A0F14"
        self.bg_panel = "#101820"
        self.neon_blue = "#00F0FF"
        self.neon_green = "#39FF14"
        self.neon_purple = "#BF00FF"
        self.neon_pink = "#FF00FF"
        self.neon_red = "#FF0055"
        self.text_white = "#E2E8F0"
        
        self.login_success = False
        
        # สร้าง UI หน้าล็อคอิน
        self.create_login_ui()
    
    def create_login_ui(self):
        # Header
        header = tk.Frame(self.root, bg=self.bg_dark, pady=30)
        header.pack(fill=tk.X)
        
        tk.Label(header, text="🔐 CYBORG NEXUS", 
                 bg=self.bg_dark, fg=self.neon_purple,
                 font=("Courier New", 24, "bold")).pack()
        tk.Label(header, text="v3.6 - LOGIN REQUIRED", 
                 bg=self.bg_dark, fg=self.neon_blue,
                 font=("Courier New", 12)).pack(pady=(5, 0))
        
        # Login Form
        form_frame = tk.Frame(self.root, bg=self.bg_panel, padx=30, pady=20)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=30)
        
        tk.Label(form_frame, text="USER ID", 
                 bg=self.bg_panel, fg=self.neon_green,
                 font=("Courier New", 12, "bold")).pack(anchor='w', pady=(10, 5))
        
        self.user_id_entry = tk.Entry(form_frame, font=("Courier New", 14), width=25,
                                    bg="#000000", fg=self.neon_blue, bd=0, relief=tk.FLAT)
        self.user_id_entry.pack(fill=tk.X, ipady=8)
        self.user_id_entry.focus()
        
        # แสดงไอดีที่ได้รับอนุญาตแล้ว
        tk.Label(form_frame, text="\nไอดีที่ได้รับอนุญาต:", 
                 bg=self.bg_panel, fg=self.neon_pink,
                 font=("Tahoma", 10)).pack(anchor='w')
        tk.Label(form_frame, text="sirisakboy", 
                 bg=self.bg_panel, fg=self.neon_green,
                 font=("Courier New", 12, "bold")).pack(anchor='w')
        
        # Unlock Code
        tk.Label(form_frame, text="\nUNLOCK CODE", 
                 bg=self.bg_panel, fg=self.neon_green,
                 font=("Courier New", 12, "bold")).pack(anchor='w', pady=(15, 5))
        
        self.unlock_code_entry = tk.Entry(form_frame, font=("Courier New", 14), width=25,
                                        bg="#000000", fg=self.neon_purple, bd=0, relief=tk.FLAT, show="*")
        self.unlock_code_entry.pack(fill=tk.X, ipady=8)
        
        # Show/Hide unlock code
        self.show_unlock_var = tk.BooleanVar()
        show_chk = tk.Checkbutton(form_frame, text="👁️ แสดงโค้ดถอนการล็อค",
                                variable=self.show_unlock_var,
                                command=self.toggle_unlock_visibility,
                                bg=self.bg_panel, fg=self.neon_blue,
                                font=("Tahoma", 9))
        show_chk.pack(pady=10)
        
        # Login Button
        self.login_btn = tk.Button(form_frame, text="🔓 UNLOCK", 
                                 command=self.attempt_login,
                                 font=("Courier New", 14, "bold"),
                                 bg="#1A2F25", fg=self.neon_green,
                                 relief=tk.FLAT, bd=0, padx=20, pady=8)
        self.login_btn.pack(pady=20)
        
        # Status
        self.status_lbl = tk.Label(form_frame, text="", 
                                  bg=self.bg_panel, fg=self.neon_red,
                                  font=("Courier New", 10))
        self.status_lbl.pack()
        
        # Footer
        footer = tk.Frame(self.root, bg=self.bg_dark, pady=20)
        footer.pack(fill=tk.X)
        tk.Label(footer, text=">> SYSTEM READY FOR AUTHORIZED USER", 
                 bg=self.bg_dark, fg=self.neon_blue,
                 font=("Courier New", 10)).pack()
        
        # Bind Enter key
        self.root.bind('<Return>', self.attempt_login)
    
    def toggle_unlock_visibility(self):
        show = self.show_unlock_var.get()
        self.unlock_code_entry.config(show="" if show else "*")
    
    def attempt_login(self, event=None):
        user_id = self.user_id_entry.get().strip()
        unlock_code = self.unlock_code_entry.get().strip()
        
        if user_id == "sirisakboy":
            self.login_success = True
            self.status_lbl.configure(text="✅ ยินดีต้อนรับ sirisakboy!", fg=self.neon_green)
            self.root.after(1000, self.root.destroy)
        else:
            self.status_lbl.configure(text="❌ ไม่ผ่านการยืนยัน! ไอดีผู้ใช้ไม่ถูกต้อง", fg=self.neon_red)
            self.user_id_entry.delete(0, tk.END)
            self.unlock_code_entry.delete(0, tk.END)
            self.user_id_entry.focus()


class UltimateCyborgTool:
    def __init__(self, root):
        self.root = root
        self.root.title("CYBORG NEXUS v3.6")
        self.root.geometry("460x720") 
        self.root.resizable(False, False)
        self.root.attributes('-topmost', True) # ตรึงบนสุดหน้าจอเสมอ
        
        # Terminal visibility state
        self.terminal_visible = True
        
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
        header_frame = tk.Frame(self.root, bg=self.bg_dark, pady=5, padx=15)
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
        
        # Settings button for API Key configuration
        self.settings_btn = tk.Button(btn_frame, text="⚙️", command=self.open_settings,
                               font=("Courier New", 9, "bold"), bg="#2A1F3D", 
                               fg=self.neon_purple, relief=tk.FLAT, bd=1)
        self.settings_btn.pack(side=tk.LEFT, padx=1, fill=tk.X, expand=True)
        
        # Import document button for CODE/UI_DESIGN modes
        self.import_btn = tk.Button(btn_frame, text="📄", command=self.import_document,
                               font=("Courier New", 9, "bold"), bg="#2A1F3D", 
                               fg=self.neon_green, relief=tk.FLAT, bd=1)
        self.import_btn.pack(side=tk.LEFT, padx=1, fill=tk.X, expand=True)
        
        # Terminal toggle button
        self.term_btn = tk.Button(btn_frame, text="💻", command=self.toggle_terminal,
                                font=("Courier New", 9, "bold"), bg="#1A2030", 
                                fg=self.neon_green, relief=tk.FLAT, bd=1)
        self.term_btn.pack(side=tk.LEFT, padx=1, fill=tk.X, expand=True)

        # Create remaining UI
        # Create remaining UI
        self.create_ui_rest()
        
        # Auto-login on startup (after UI is ready)
        self.root.after(1000, self.do_login)

    def on_provider_select(self):
        """Auto-login when provider is selected"""
        self.do_login()

    def open_settings(self):
        """เปิดหน้าต่างตั้งค่าครบถ้วน"""
        settings_win = tk.Toplevel(self.root)
        settings_win.title("⚙️ ตั้งค่า CYBORG NEXUS")
        settings_win.geometry("500x650")
        settings_win.configure(bg=self.bg_dark)
        settings_win.resizable(False, False)
        settings_win.transient(self.root)
        settings_win.grab_set()
        
        # Create notebook (tabs)
        notebook = ttk.Notebook(settings_win)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Style for notebook
        style = ttk.Style()
        style.configure("TNotebook", background=self.bg_dark)
        style.configure("TNotebook.Tab", background=self.bg_panel, foreground=self.text_white)
        
        # === TAB 1: API Keys ===
        api_tab = tk.Frame(notebook, bg=self.bg_dark)
        notebook.add(api_tab, text="🔑 API Keys")
        
        tk.Label(api_tab, text="🔑 API Key Configuration", 
                 bg=self.bg_dark, fg=self.neon_purple, 
                 font=("Courier New", 12, "bold")).pack(pady=10)
        
        providers = [
            ("OpenAI API Key", "OPENAI_API_KEY"),
            ("Gemini API Key", "GEMINI_API_KEY"),
            ("Ollama Model", "OLLAMA_MODEL")
        ]
        self.api_entries = {}
        for i, (label, key) in enumerate(providers):
            tk.Label(api_tab, text=label, bg=self.bg_dark, 
                     fg=self.text_white, font=("Tahoma", 10)).pack(pady=(10,0), anchor='w', padx=20)
            entry = tk.Entry(api_tab, width=45, font=("Courier New", 10), 
                           bg=self.bg_panel, fg=self.neon_green, show="*")
            entry.pack(pady=2, padx=20, anchor='w')
            saved = os.environ.get(key, "")
            if saved and saved != "sk-your-openai-api-key-here":
                entry.insert(0, saved)
            self.api_entries[key] = entry
        
        # Show/Hide password toggle
        self.show_pwd_var = tk.BooleanVar()
        show_chk = tk.Checkbutton(api_tab, text="👁️ แสดงรหัสผ่าน", 
                                variable=self.show_pwd_var,
                                command=self.toggle_password_visibility,
                                bg=self.bg_dark, fg=self.neon_blue,
                                font=("Tahoma", 9))
        show_chk.pack(pady=10)
        
        # === TAB 2: Model Selection ===
        model_tab = tk.Frame(notebook, bg=self.bg_dark)
        notebook.add(model_tab, text="🤖 Models")
        
        tk.Label(model_tab, text="🤖 เลือก AI Model", 
                 bg=self.bg_dark, fg=self.neon_blue, 
                 font=("Courier New", 12, "bold")).pack(pady=10)
        
        # TGPT Provider selection
        tk.Label(model_tab, text="TGPT Provider", bg=self.bg_dark, 
                 fg=self.text_white, font=("Tahoma", 10)).pack(anchor='w', padx=20)
        self.model_provider_var = tk.StringVar(value=self.sub_option_var.get())
        model_combo = ttk.Combobox(model_tab, textvariable=self.model_provider_var,
                                 font=("Tahoma", 10), width=30)
        model_combo["values"] = ["sky", "pollinations", "deepseek", "groq", "ollama"]
        model_combo.pack(pady=5, padx=20)
        
        # Ollama models
        tk.Label(model_tab, text="Ollama Models (เมื่อเลือก ollama)", 
                 bg=self.bg_dark, fg=self.neon_green, font=("Tahoma", 9)).pack(anchor='w', padx=25)
        self.ollama_model_var = tk.StringVar(value=os.environ.get("OLLAMA_DEFAULT_MODEL", "llama3"))
        ollama_combo = ttk.Combobox(model_tab, textvariable=self.ollama_model_var,
                                    font=("Tahoma", 9), width=25)
        ollama_combo["values"] = ["llama3", "llama3.2", "mistral", "codellama", "phi3", "gemma", "qwen2.5"]
        ollama_combo.pack(pady=5, padx=20)
        
        # === TAB 3: Prompt Templates ===
        prompt_tab = tk.Frame(notebook, bg=self.bg_dark)
        notebook.add(prompt_tab, text="💬 Prompts")
        
        tk.Label(prompt_tab, text="💬 ปรับแต่ง Prompt Template", 
                 bg=self.bg_dark, fg=self.neon_yellow, 
                 font=("Courier New", 12, "bold")).pack(pady=10)
        
        self.prompt_templates = {}
        modes_th = [
            ("UI_DESIGN", "UI/UX ออกแบบ"),
            ("CODE", "โค้ดโปรแกรม"),
            ("BUG_SCAN", "สแกนบั๊ก"),
            ("IMAGE", "สร้างภาพ")
        ]
        
        for mode, label in modes_th:
            tk.Label(prompt_tab, text=f"{label} Prompt", bg=self.bg_dark, 
                     fg=self.text_white, font=("Tahoma", 9)).pack(anchor='w', padx=20, pady=(5,0))
            txt = tk.Text(prompt_tab, width=50, height=3, font=("Courier New", 9),
                          bg=self.bg_panel, fg=self.neon_green)
            txt.pack(pady=2, padx=20)
            # โหลด template ที่บันทึกไว้
            saved_template = os.environ.get(f"PROMPT_{mode}", "")
            txt.insert("1.0", saved_template if saved_template else f"[{mode} default template]")
            self.prompt_templates[mode] = txt
        
        # === TAB 4: Language ===
        lang_tab = tk.Frame(notebook, bg=self.bg_dark)
        notebook.add(lang_tab, text="🌐 Language")
        
        tk.Label(lang_tab, text="🌐 เลือกภาษา", 
                 bg=self.bg_dark, fg=self.neon_pink, 
                 font=("Courier New", 12, "bold")).pack(pady=10)
        
        self.lang_var = tk.StringVar(value=os.environ.get("APP_LANGUAGE", "th"))
        lang_frame = tk.Frame(lang_tab, bg=self.bg_dark)
        lang_frame.pack(pady=10)
        tk.Radiobutton(lang_frame, text="ไทย (TH)", variable=self.lang_var, value="th",
                      bg=self.bg_dark, fg=self.neon_green, font=("Tahoma", 10)).pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(lang_frame, text="English (EN)", variable=self.lang_var, value="en",
                      bg=self.bg_dark, fg=self.neon_blue, font=("Tahoma", 10)).pack(side=tk.LEFT, padx=10)
        
        # === TAB 5: Cloud Sync ===
        cloud_tab = tk.Frame(notebook, bg=self.bg_dark)
        notebook.add(cloud_tab, text="☁️ Cloud")
        
        tk.Label(cloud_tab, text="☁️ ซิงค์กับ Cloud", 
                 bg=self.bg_dark, fg=self.neon_blue, 
                 font=("Courier New", 12, "bold")).pack(pady=10)
        
        tk.Label(cloud_tab, text="Sync ไฟล์ผลลัพธ์ไปยัง Cloud", 
                 bg=self.bg_dark, fg=self.text_white, font=("Tahoma", 10)).pack(pady=5)
        
        self.sync_var = tk.BooleanVar(value=os.environ.get("CLOUD_SYNC", "false").lower() == "true")
        sync_chk = tk.Checkbutton(cloud_tab, text="🔄 เปิดใช้ Cloud Sync", 
                                  variable=self.sync_var,
                                  bg=self.bg_dark, fg=self.neon_green,
                                  font=("Tahoma", 10))
        sync_chk.pack(pady=5)
        
        tk.Label(cloud_tab, text="Webhook URL (optional)", bg=self.bg_dark, 
                 fg=self.text_white, font=("Tahoma", 9)).pack(anchor='w', padx=20, pady=(10,0))
        self.webhook_entry = tk.Entry(cloud_tab, width=45, font=("Courier New", 9),
                                      bg=self.bg_panel, fg=self.neon_blue)
        self.webhook_entry.pack(pady=2, padx=20)
        webhook_saved = os.environ.get("WEBHOOK_URL", "")
        if webhook_saved:
            self.webhook_entry.insert(0, webhook_saved)
        
        # Save button for all tabs
        btn_frame = tk.Frame(settings_win, bg=self.bg_dark)
        btn_frame.pack(pady=15)
        tk.Button(btn_frame, text="💾 บันทึกทั้งหมด", command=self.save_all_settings,
                  bg=self.bg_panel, fg=self.neon_green,
                  font=("Courier New", 10, "bold")).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="❌ ปิด", command=settings_win.destroy,
                  bg=self.bg_panel, fg=self.neon_red,
                  font=("Courier New", 10, "bold")).pack(side=tk.LEFT, padx=5)

    def toggle_password_visibility(self):
        """Toggle password visibility in settings"""
        show = self.show_pwd_var.get()
        for entry in self.api_entries.values():
            entry.config(show="" if show else "*")

    def save_all_settings(self):
        """บันทึกการตั้งค่าทั้งหมด"""
        # Save API Keys
        for key, entry in self.api_entries.items():
            value = entry.get().strip()
            if value:
                os.environ[key] = value
        
        # Save Model settings
        os.environ["TGPT_PROVIDER"] = self.model_provider_var.get()
        os.environ["OLLAMA_DEFAULT_MODEL"] = self.ollama_model_var.get()
        
        # Save Prompt templates
        for mode, txt_widget in self.prompt_templates.items():
            template = txt_widget.get("1.0", tk.END).strip()
            if template and "default" not in template.lower():
                os.environ[f"PROMPT_{mode}"] = template
        
        # Save Language
        os.environ["APP_LANGUAGE"] = self.lang_var.get()
        
        # Save Cloud settings
        os.environ["CLOUD_SYNC"] = "true" if self.sync_var.get() else "false"
        webhook = self.webhook_entry.get().strip()
        if webhook:
            os.environ["WEBHOOK_URL"] = webhook
        
        try:
            # Save to .env file
            env_path = os.path.join(BASE_PATH, ".env")
            with open(env_path, "w") as f:
                for key in self.api_entries.keys():
                    f.write(f"{key}={self.api_entries[key].get().strip()}\n")
                f.write(f"TGPT_PROVIDER={self.model_provider_var.get()}\n")
                f.write(f"OLLAMA_DEFAULT_MODEL={self.ollama_model_var.get()}\n")
                for mode, txt_widget in self.prompt_templates.items():
                    template = txt_widget.get("1.0", tk.END).strip()
                    if template and "default" not in template.lower():
                        f.write(f"PROMPT_{mode}={template}\n")
                f.write(f"APP_LANGUAGE={self.lang_var.get()}\n")
                f.write(f"CLOUD_SYNC={'true' if self.sync_var.get() else 'false'}\n")
                if webhook:
                    f.write(f"WEBHOOK_URL={webhook}\n")
            messagebox.showinfo("SUCCESS", "บันทึกการตั้งค่าทั้งหมดสำเร็จ!")
        except Exception as e:
            messagebox.showerror("ERROR", f"บันทึกล้มเหลว: {str(e)}")

    def import_document(self):
        """นำเข้าไฟล์เอกสารเพื่อวิเคราะห์โค้ด/UI - ไม่จำกัดความยาว"""
        file_path = filedialog.askopenfilename(
            filetypes=[("Document Files", "*.txt *.md *.py *.js *.ts *.tsx *.jsx *.html *.css *.scss *.json *.xml *.yaml *.yml *.cpp *.c *.h *.hpp *.java *.cs *.go *.rs *.rb *.php *.swift *.kt *.scala *.sql *.sh *.bat *.ps1")]
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                # ใส่เนื้อหาลงใน cmd_entry - ไม่จำกัดความยาว
                self.cmd_entry.delete("1.0", tk.END)
                self.cmd_entry.insert("1.0", f"# File: {os.path.basename(file_path)}\n\n{content}")
                self.log_terminal(f"Loaded: {os.path.basename(file_path)} ({len(content)} chars)")
                messagebox.showinfo("SUCCESS", f"โหลดไฟล์สำเร็จ!\n{os.path.basename(file_path)}\nขนาด: {len(content)} ตัวอักษร")
            except Exception as e:
                messagebox.showerror("ERROR", f"ไม่สามารถอ่านไฟล์: {str(e)}")

    def do_code_review(self):
        """เลือกโฟลเดอร์โปรเจ็กต์เพื่อรีวิวโค้ดทั้งหมด"""
        folder_path = filedialog.askdirectory(title="เลือกโฟลเดอร์โปรเจ็กต์")
        if not folder_path:
            return
        
        # ประเมินขนาดโฟลเดอร์
        total_size = 0
        file_count = 0
        code_files = []
        
        supported_exts = ['.py', '.js', '.ts', '.jsx', '.tsx', '.html', '.css', '.scss', 
                          '.java', '.cpp', '.c', '.h', '.hpp', '.cs', '.go', '.rs', '.rb', '.php',
                          '.swift', '.kt', '.scala', '.sql', '.sh', '.bat', '.ps1', '.json', '.xml', '.yaml', '.yml', '.md', '.txt']
        
        for root_dir, dirs, files in os.walk(folder_path):
            # ข้ามโฟลเดอร์ .git และ node_modules
            dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '__pycache__', 'venv', '.venv', 'dist', 'build']]
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in supported_exts:
                    file_path = os.path.join(root_dir, file)
                    try:
                        size = os.path.getsize(file_path)
                        total_size += size
                        if total_size < 50000:  # จำกัดที่ 50KB ต่อครั้ง
                            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                content = f.read()
                            code_files.append(f"// {os.path.relpath(file_path, folder_path)}\n{content}")
                            file_count += 1
                    except Exception:
                        continue
        
        if not code_files:
            messagebox.showwarning("WARNING", "ไม่พบไฟล์โค้ดในโฟลเดอร์นี้!")
            return
        
        # สร้าง prompt สำหรับรีวิว
        all_code = "\n\n".join(code_files[:20])  # ส่งไฟล์ 20 ไฟล์แรก
        prompt = f"ทำการ Code Review ให้โค้ดจากโฟลเดอร์:\n{os.path.basename(folder_path)}\n\nไฟล์ที่รีวิว: {file_count} ไฟล์\n\nโค้ด:\n{all_code}"
        
        self.log_text.pack_forget()
        self.log_text.delete(1.0, tk.END)
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        self.call_worker_api(prompt, is_design=False)
        
        messagebox.showinfo("CODE_REVIEW", f"กำลังรีวิว {file_count} ไฟล์จากโฟลเดอร์\n{os.path.basename(folder_path)}")

    def create_ui_rest(self):
        input_frame = tk.LabelFrame(self.root, text=" [ ENTER_COMMAND_PROMPT ] ", font=("Courier New", 9, "bold"),
                                    fg=self.neon_blue, bg=self.bg_dark, bd=1, relief=tk.SOLID)
        input_frame.pack(fill=tk.X, padx=15, pady=5)
        
        self.cmd_entry = tk.Text(input_frame, font=("Tahoma", 12), bg=self.bg_panel, fg=self.text_white, 
                                  insertbackground=self.neon_blue, bd=0, highlightthickness=1, highlightbackground="#223344", height=5, wrap=tk.WORD)
        self.cmd_entry.pack(fill=tk.X, padx=8, pady=8)

        # --- [3. MODE SELECTOR (เพิ่มตัวเลือก BUG_SCAN)] ---
        mode_frame = tk.Frame(self.root, bg=self.bg_dark)
        mode_frame.pack(fill=tk.X, padx=15, pady=2)
        
        self.current_mode = tk.StringVar(value="UI_DESIGN")
        
        modes = [
            ("🎨 UI_DESIGN", "UI_DESIGN"), 
            ("💻 CODE", "CODE"), 
            ("🔍 BUG_SCAN", "BUG_SCAN"),
            ("📂 CODE_REVIEW", "CODE_REVIEW"),  # 🆕 รีวิวโค้ดโปรเจ็กต์ทั้งหมด
            ("🖼️ IMAGE", "IMAGE")
        ]
        for text, mode_val in modes:
            rb = tk.Radiobutton(mode_frame, text=text, variable=self.current_mode, value=mode_val,
                                font=("Courier New", 8, "bold"), fg=self.text_white, bg=self.bg_dark,
                                activebackground=self.bg_dark, activeforeground=self.neon_blue,
                                selectcolor=self.bg_panel, indicatoron=0, bd=1, relief=tk.FLAT, padx=4, pady=4)
            rb.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=1)

        # --- [4. DISPLAY & OUTPUT LOG PANEL] ---
        self.display_frame = tk.LabelFrame(self.root, text=" [ OUTPUT ] ", font=("Courier New", 9, "bold"),
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

        # --- [3.5 TERMINAL OUTPUT PANEL] ---
        self.terminal_frame = tk.LabelFrame(self.root, text=" [ TERMINAL LOG ] ", font=("Courier New", 9, "bold"),
                                            fg=self.neon_green, bg=self.bg_dark, bd=1, relief=tk.SOLID)
        self.terminal_frame.pack(fill=tk.X, padx=15, pady=2)
        
        self.terminal_text = tk.Text(self.terminal_frame, height=6, font=("Courier New", 9), 
                                     bg="#000000", fg=self.neon_green, bd=0, insertbackground=self.neon_green)
        self.terminal_text.pack(fill=tk.X, padx=5, pady=3)
        self.terminal_text.insert(tk.END, ">> TERMINAL READY.\n>> Output will appear here...\n")
        
        # --- [4. STATUS BAR] ---
        self.status_bar = tk.Label(self.root, text="[ WAITING ]", 
                                font=("Courier New", 8, "bold"), fg=self.neon_yellow, bg=self.bg_dark)
        self.status_bar.pack(fill=tk.X, padx=15, pady=2)

        # --- [6. PROGRESS BAR] ---
        self.progress = tk.ttk.Progressbar(
            self.root, orient=tk.HORIZONTAL, mode='indeterminate'
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

    def toggle_terminal(self):
        """Toggle terminal visibility"""
        if self.terminal_visible:
            self.terminal_frame.pack_forget()
            self.term_btn.configure(fg=self.neon_red)
        else:
            self.terminal_frame.pack(fill=tk.X, padx=15, pady=2)
            self.term_btn.configure(fg=self.neon_green)
        self.terminal_visible = not self.terminal_visible

    def log_terminal(self, message):
        """Log message to terminal panel"""
        if hasattr(self, 'terminal_text') and self.terminal_text:
            self.terminal_text.insert(tk.END, message + "\n")
            self.terminal_text.see(tk.END)

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

            # Cloud Sync - ส่งไฟล์ไปยัง Webhook หากเปิดใช้
            self.sync_to_cloud(filepath, mode)

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

    def sync_to_cloud(self, filepath, mode):
        """ซิงค์ไฟล์ผลลัพธ์ไปยัง Cloud Webhook"""
        webhook = os.environ.get("WEBHOOK_URL", "")
        cloud_sync = os.environ.get("CLOUD_SYNC", "false").lower() == "true"
        
        if not webhook or not cloud_sync:
            return
        
        try:
            with open(filepath, "rb") as f:
                files = {"file": (os.path.basename(filepath), f, "text/plain")}
                data = {"mode": mode, "timestamp": datetime.now().isoformat()}
                requests.post(webhook, files=files, data=data, timeout=10)
            self.log_text.insert(tk.END, "\n>> CLOUD SYNC: Completed\n")
        except Exception as e:
            err_msg = str(e)[:50]
            self.log_text.insert(tk.END, f"\n>> CLOUD SYNC: Failed ({err_msg})\n")

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
        self.log_terminal(f"\n=== MODE: {mode} ===")
        
        # ตรวจจับเนื้อหาจากไฟล์ที่ถูกนำเข้า
        file_content = None
        file_name = None
        if prompt.startswith("# File:"):
            # แยกเนื้อหาจากไฟล์
            parts = prompt.split("\n\n", 1)
            if len(parts) > 1:
                file_name = parts[0].replace("# File:", "").strip()
                file_content = parts[1]
            else:
                file_content = prompt
        
        if mode == "BUG_SCAN":
            if not self.image_path:
                messagebox.showwarning("WARNING", "กรุณากดปุ่ม UPLOAD SCREENSHOT เพื่อเลือกภาพหน้าจอบั๊กก่อน!")
                return
            self.call_worker_vision_api()
        elif mode == "UI_DESIGN":
            # หากมีเนื้อหาจากไฟล์ ให้ปรับ prompt ให้เหมาะกับการวิเคราะห์ UI - ไม่จำกัดความยาว
            if file_content:
                prompt = f"วิเคราะห์โค้ด/UI จากไฟล์ '{file_name}' และให้ข้อเสนอแนะการออกแบบ: {file_content}"
            elif not prompt or prompt.startswith("เช่น"):
                messagebox.showwarning("WARNING", "กรุณากรอกคำสั่งบรีฟงานด้วย!")
                return
            self.call_worker_api(prompt, is_design=True)
        elif mode == "CODE":
            # หากมีเนื้อหาจากไฟล์ ให้ปรับ prompt ให้เหมาะกับการวิเคราะห์โค้ด
            if file_content:
                prompt = f"วิเคราะห์โค้ดจากไฟล์ '{file_name}' และอธิบาย/ปรับปรุง: {file_content}"
            elif not prompt or prompt.startswith("เช่น"):
                messagebox.showwarning("WARNING", "กรุณากรอกคำสั่งบรีฟงานด้วย!")
                return
            self.call_worker_api(prompt, is_design=False)
        elif mode == "CODE_REVIEW":
            # เลือกโฟลเดอร์โปรเจ็กต์เพื่อรีวิวโค้ด
            self.do_code_review()
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
        self.log_terminal(f">>> CONNECTING TO {provider.upper()} AI...")
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
    # สร้างหน้าต่างล็อคอินก่อน
    if USE_DND:
        login_root = TkinterDnD.Tk()
    else:
        login_root = tk.Tk()
    
    login_win = LoginWindow(login_root)
    login_root.mainloop()
    
    # ถ้าล็อคอินสำเร็จ ให้เปิดหน้าหลัก
    if login_win.login_success:
        if USE_DND:
            root = TkinterDnD.Tk()
        else:
            root = tk.Tk()
        app = UltimateCyborgTool(root)
        root.mainloop()
