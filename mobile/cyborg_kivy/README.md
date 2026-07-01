# CYBORG NEXUS Mobile - Kivy Edition

เวอร์ชันมือถือของ CYBORG NEXUS ที่พัฒนาด้วย Kivy Framework

## ฟีเจอร์หลัก

### 🔍 BUG_SCAN Mode (มี Camera ในมือถือ!)
- ถ่ายภาพจากกล้องโดยตรงในมือถือ
- เลือกรูปจากแกเลอรี่
- ส่งภาพไปวิเคราะห์ข้อผิดพลาดผ่าน Gemini Vision API

### 🎨 UI_DESIGN Mode
- ออกแบบ UI/UX และได้รับคำแนะนำจาก AI

### 💻 CODE Mode
- สร้างและอธิบายโค้ดโปรแกรม

### 🖼️ IMAGE Mode
- สร้างภาพจาก AI

## การติดตั้งบน Android

### ขั้นตอนที่ 1: ติดตั้ง Buildozer
```bash
pip install buildozer
```

### ขั้นตอนที่ 2: Build APK
```bash
cd mobile/cyborg_kivy
buildozer -v android debug
```

### ขั้นตอนที่ 3: ติดตั้ง APK จาก output
```
output/apk/*.apk
```

## การรันบน Desktop (ทดสอบ)

```bash
pip install kivy pillow requests
python main.py
```

## การตั้งค่า API Key

ต้องตั้งค่า GEMINI_API_KEY ใน environment variables เพื่อใช้งาน BUG_SCAN

```bash
export GEMINI_API_KEY=your_api_key_here
```

หรือใส่ในไฟล์ `.env`