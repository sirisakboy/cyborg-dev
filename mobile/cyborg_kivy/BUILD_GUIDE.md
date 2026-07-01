# คำแนะนำการ Build Android APK

## วิธีที่ 1: ใช้ GitHub Actions (CI/CD) - อัตโนมัติ

Workflow ได้ถูกตั้งค่าที่ `.github/workflows/build-android.yml` แล้ว

### วิธีใช้:
1. Push โค้ดไปยัง branch `main`
2. ไปที่แท็บ **Actions** ใน GitHub เพื่อดูสถานะการ build
3. APK จะถูกอัปโลดเป็น artifact หลังจาก build เสร็จ
   - หรือสามารถดาวน์โหลดจาก releases (ถ้าสร้าง tag)

### ข้อแม้ CI Build:
- ใช้เวลา 20-60 นาที (ขึ้นกับ network)
- ต้องใช้ cache เพื่อความเร็ว
- ครั้งแรกอาจใช้เวลานาน

---

## วิธีที่ 2: Build บนคอมพิวเตอร์ของคุณ (แนะนำ)

### ขั้นตอน:

#### Linux/Ubuntu:
```bash
# ติดตั้ง dependencies
sudo apt-get update
sudo apt-get install -y python3-pip python3-setuptools python3-wheel \
    zipalign openjdk-11-jdk autoconf libtool libssl-dev libffi-dev \
    python3-dev zlib1g-dev libpng-dev libncurses5-dev unzip git ccache

# ติดตั้ง buildozer
pip3 install --user buildozer cython

# Build APK
cd mobile/cyborg_kivy
buildozer android debug
```

#### Windows (WSL):
```bash
# เปิด WSL
wsl

# ติดตั้ง dependencies เหมือน Linux
sudo apt-get update
sudo apt-get install -y python3-pip ... (เหมือนด้านบน)

# Build APK
cd /mnt/c/Users/AutoBoy/cyborg-dev/mobile/cyborg_kivy
buildozer android debug
```

#### macOS:
```bash
brew install python3 autoconf libtool openssl
pip3 install buildozer cython
cd mobile/cyborg_kivy
buildozer android debug
```

### ไฟล์ที่ได้:
```
mobile/cyborg_kivy/bin/CyborgKivyApp-1.0-debug.apk
```

---

## การตั้งค่า API Key

ดาวน์โหลด APK แล้วต้องตั้งค่า GEMINI_API_KEY เพื่อใช้งาน BUG_SCAN

### วิธี:
1. สร้างไฟล์ `.env` ในโฟลเดอร์ `output/` บนมือถือ
2. หรือใส่ API Key ในแอป Settings หลังจากติดตั้ง

---

## Troubleshooting

### ปัญหา: SDK licenses
```bash
# ยอมรับ licenses
yes | $HOME/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager --licenses
```

### ปัญหา: NDK ไม่พบ
- ตรวจสอบ `android.sdk_path` และ `android.ndk_path` ใน `buildozer.spec`

### ปัญหา: Camera ไม่ทำงานบน Android
- แอปจะขอ permission อัตโนมัติ
- ตรวจสอบว่าเปิด CAMERA permission ใน Settings ของ Android