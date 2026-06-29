# CYBORG NEXUS v3.5

เครื่องมือ GUI ที่ขับเคลื่อนด้วย AI สำหรับการออกแบบ UI/UX, การสร้างโค้ด, การสแกนหาบั๊ก & การสร้างภาพ

## คุณสมบัติหลัก

- 🎨 **UI_DESIGN** - สร้างการออกแบบ UI/UX ด้วย AI
- 💻 **CODE** - สร้างโค้ดจากคำอธิบาย  
- 🔍 **BUG_SCAN** - วิเคราะห์ภาพหน้าจอเพื่อหาบั๊ก (รองรับลาก & วาง)
- 🖼️ **IMAGE** - สร้างภาพจากคำอธิบายข้อความ

## 🚀 เริ่มต้นใช้งานอย่างรวดเร็ว

### ตัวเลือก 1: การติดตั้งอัตโนมัติ (แนะนำ)
รันตัวติดตั้งที่เหมาะสมสำหรับแพลตฟอร์มของคุณ:

**Windows:**
```batch
install-windows.bat
```

**Linux/macOS:**
```bash
chmod +x install-linux.sh
./install-linux.sh
```

### ตัวเลือก 2: การติดตั้งด้วยตนเอง
```bash
# 1. โคลนที่เก็บข้อมูล
git clone <repository-url>
cd cyborg-dev

# 2. ติดตั้งการพึ่งพา Python
pip install -r requirements.txt

# 3. ติดตั้ง TGPT (สำหรับการทำงานเต็มรูปแบบ)
# Windows: ดาวน์โหลดจาก https://github.com/aandrew-me/tgpt/releases
# Linux: curl -sSf https://raw.githubusercontent.com/aandrew-me/tgpt/master/install.sh | sh
# macOS: brew install tgpt

# 4. รันแอปพลิเคชัน
python main.py
```

## 📋 คู่มือการติดตั้งตามแพลตฟอร์ม

### Windows
1. ติดตั้ง Python 3.8+ จาก https://python.org
2. ติดตั้ง TGPT:
   - ดาวน์โหลดรุ่นล่าสุดจาก https://github.com/aandrew-me/tgpt/releases
   - แตกไฟล์และเพิ่มเข้าไปใน PATH, หรือใช้ตัวติดตั้ง
3. ติดตั้งการพึ่งพา Python:
   ```batch
   pip install -r requirements.txt
   ```
4. รัน: `python main.py`

### Linux (Ubuntu/Debian)
```bash
# ติดตั้งการพึ่งพา
sudo apt update
sudo apt install python3 python3-pip python3-tk -y

# ติดตั้ง TGPT
curl -sSf https://raw.githubusercontent.com/aandrew-me/tgpt/master/install.sh | sh

# ติดตั้งการพึ่งพา Python
pip3 install -r requirements.txt

# รัน
python3 main.py
```

### Linux (Fedora/CentOS/RHEL)
```bash
# ติดตั้งการพึ่งพา
sudo dnf install python3 python3-pip python3-tkinter -y

# ติดตั้ง TGPT
curl -sSf https://raw.githubusercontent.com/aandrew-me/tgpt/master/install.sh | sh

# ติดตั้งการพึ่งพา Python
pip3 install -r requirements.txt

# รัน
python3 main.py
```

### macOS
```bash
# ติดตั้งการพึ่งพา (ใช้ Homebrew)
brew install python tk

# ติดตั้ง TGPT
brew install tgpt

# ติดตั้งการพึ่งพา Python
pip3 install -r requirements.txt

# รัน
python3 main.py
```

## 🔧 การตั้งค่า

### ตัวแปรสภาพแวดล้อม
สร้างไฟล์ `.env` ในไดเรกทอรีรากของโครงการ:

```env
# คีย์ API OpenAI (สำหรับผู้ให้บริการ OpenAI)
OPENAI_API_KEY=your_openai_api_key_here

# คีย์ API Google (สำหรับผู้ให้บริการ Google)
GEMINI_API_KEY=your_google_api_key_here

# คีย์ API Anthropic (สำหรับผู้ให้บริการ Anthropic)
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# ผู้ให้บริการ TGPT (ค่าเริ่มต้น: sky)
TGPT_PROVIDER=sky

# ผู้ให้บริการสร้างภาพ (ค่าเริ่มต้น: pollinations)
IMG_PROVIDER=pollinations
```

## 🖥️ คู่มือการใช้งาน

### ผู้ให้บริการ AI
CYBORG NEXUS รองรับผู้ให้บริการ AI หลายราย:

| ผู้ให้บริการ | จำเป็นต้องตั้งค่า | เหมาะสำหรับ |
|--------------|-------------------|-------------|
| **TGPT** | ติดตั้งไบนารี TGPT | ฟรี, ตอบสนองเร็ว |
| **OpenAI** | คีย์ API | คุณภาพสูงสุด |
| **Google/Gemini** | คีย์ API | สมดุลที่ดี |
| **Anthropic** | คีย์ API | งานเหตุผล |
| **Ollama** | การติดตั้งในเครื่อง | ความเป็นส่วนตัว, ออฟไลน์ |
| **Groq** | คีย์ API | ความเร็วสูงมาก |
| **DeepSeek** | คีย์ API | เหตุผล |

### โหมดการทำงาน
- **UI_DESIGN**: สร้างการออกแบบ UI/UX และม็อคอัพ
- **CODE**: สร้างโค้ดจากคำอธิบายภาษาธรรมชาติ
- **BUG_SCAN**: วิเคราะห์ภาพหน้าจอเพื่อหาบั๊กและปัญหา
- **IMAGE**: สร้างภาพจากคำอธิบายข้อความ

### ปุ่มลัดคีย์บอร์ด
- 📥 **อัปโหลดภาพ**: คลิกปุ่มอัปโหลดหรือลาก & วาง
- 💾 **บันทึกผลลัพธ์**: บันทึกผลลัพธ์ปัจจุบันลงไฟล์
- 📋 **คัดลอกไปยังคลิปบอร์ด**: คัดลอกข้อความผลลัพธ์
- ⚡ **ดำเนินการ**: รันพรอมต์ปัจจุบันด้วยโหมด/ผู้ให้บริการที่เลือก
- 🧹 **ล้างผลลัพธ์**: ล้างหน้าต่างผลลัพธ์
- 📤 **เปิดโฟลเดอร์ผลลัพธ์**: เปิดไดเรกทอรี generated_outputs

## 📁 ไฟล์ผลลัพธ์
เนื้อหาที่สร้างทั้งหมดจะถูกบันทึกในไดเรกทอรี `generated_outputs/`:
- ผลลัพธ์ข้อความ: ไฟล์ `.txt`
- ภาพ: ไฟล์ `.png`
- ม็อคอัพ UI: ไฟล์ `.png`

## 🐛 การแก้ไขปัญหา

### ปัญหาที่พบบ่อย

#### "ไม่พบ TGPT" หรือ "[WinError 193] %1 ไม่ใช่แอปพลิเคชัน Win32 ที่ถูกต้อง"
**วิธีแก้ไข**: ติดตั้ง TGPT สำหรับแพลตฟอร์มของคุณ:
- **Windows**: ดาวน์โหลดจาก https://github.com/aandrew-me/tgpt/releases
- **Linux**: `curl -sSf https://raw.githubusercontent.com/aandrew-me/tgpt/master/install.sh | sh`
- **macOS**: `brew install tgpt`

#### "ข้อผิดพลาดคีย์ API ไม่ถูกตั้งค่า"
**วิธีแก้ไข**: สร้างไฟล์ `.env` พร้อมคีย์ API ของคุณ:
```env
OPENAI_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
```

#### การพึ่งพา Python หายไป
**วิธีแก้ไข**: ติดตั้งการพึ่งพาใหม่:
```bash
pip install --upgrade -r requirements.txt
```

#### หน้าต่างแอปพลิเคชันไม่ตอบสนอง
**วิธีแก้ไข**: ผู้ให้บริการ AI บางรายอาจใช้เวลาในการตอบสนอง โปรดรอ 30-60 วินาทีสำหรับคำขอที่ซับซ้อน

## 📞 การสนับสนุน & การมีส่วนร่วม

สำหรับปัญหา โปรดตรวจสอบ:
1. ว่าคุณได้ติดตั้ง TGPT หรือตั้งค่าผู้ให้บริการทางเลือกแล้ว
2. ว่าคีย์ API ของคุณถูกต้อง (หากใช้ผู้ให้บริการแบบชำระเงิน)
3. ว่าคุณมีการเชื่อมต่ออินเทอร์เน็ตสำหรับผู้ให้บริการออนไลน์

ยินดีต้อนรับการมีส่วนร่วม! โปรดส่ง Pull Requests ได้เลย

## 📄 ใบอนุญาต

ใบอนุญาต MIT - ดูไฟล์ [LICENSE](LICENSE) สำหรับรายละเอียด

## 🙏 คำขอบคุณ

- [TGPT](https://github.com/aandrew-me/tgpt) - เครื่องมือ CLI AI ที่หลากหลาย
- ผู้ให้บริการ AI ทั้งหมดที่รวมไว้ (OpenAI, Google, Anthropic, เป็นต้น)
- ชุมชนโอเพ่นซอร์สสำหรับส่วนประกอบต่างๆ ที่ใช้