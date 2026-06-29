# คู่มือการติดตั้ง Flutter สำหรับหลายแพลตฟอร์ม (ภาษาไทย)

คู่มือนี้ให้ขั้นตอนการติดตั้ง Flutter และ Android SDK บนระบบปฏิบัติการต่างๆ รวมถึง Ubuntu, Debian, Kali Linux, Fedora, Termux และ Windows โดยอิงตามหลักการจาก https://github.com/mumumusuc/termux-flutter.git

## 📋 **วิธีการติดตั้งที่มีให้เลือก**

### 1. **สคริปต์ติดตั้งแบบหลายแพลตฟอร์ม (แนะนำ)**
```bash
./install_flutter_multiplatform.sh
```
- **รองรับ**: Ubuntu, Debian, Kali Linux, Fedora, Termux
- **คุณสมบัติ**: ตรวจจับระบบปฏิบัติการอัตโนมัติ, ติดตั้งทุกอย่างที่จำเป็น, ตั้งค่า Flutter + Android SDK
- **อิงตาม**: หลักการจาก https://github.com/mumumusuc/termux-flutter.git

### 2. **สคริปต์ติดตั้งเฉพาะแพลตฟอร์ม**
#### Ubuntu/Debian/Kali Linux:
```bash
./install_flutter_ubuntu.sh
```

#### Fedora/RHEL/CentOS:
```bash
./install_flutter_fedora.sh
```

#### Termux (Android):
```bash
./install_flutter_termux.sh
```

### 3. **การติดตั้งบน Windows**
ดูรายละเอียดในไฟล์: `install_flutter_windows.md`

## 🔧 **สิ่งที่จะได้รับหลังการติดตั้ง**

### ✅ **ส่วนประกอบหลัก**
- **Flutter SDK** (เวอร์ชันล่าสุดที่เสถียรจากคลังอย่างเป็นทางการ)
- **Android SDK** ประกอบด้วย:
  - เครื่องมือแพลตฟอร์ม (adb, fastboot)
  - เครื่องมือสร้าง (เวอร์ชัน 33.0.2)
  - แพลตฟอร์ม Android (API 33 - Android 13.0)
- **OpenJDK 17** (จำเป็นสำหรับการพัฒนา Android)
- **เครื่องมือพื้นฐาน**: git, wget, unzip, zip, clang

### ✅ **การตั้งค่าสภาพแวดล้อม**
- การตั้งค่าตัวแปรสภาพแวดล้อม `ANDROID_SDK_ROOT` อัตโนมัติ
- การเพิ่ม Flutter และ Android platform-tools เข้าใน `PATH` อัตโนมัติ
- การตั้งค่าถาวรผ่านไฟล์ `~/.bashrc` (หรือเทียบเท่า)

### ✅ **การตรวจสอบ**
- การตรวจสอบอัตโนมัติด้วย `flutter --version` และ `flutter doctor`
- การขออนุญาตสำหรับใบอนุญาต Android

## 🖥️ **รายละเอียดเฉพาะแพลตฟอร์ม**

### **Ubuntu/Debian/Kali Linux**
- ใช้ตัวจัดการแพ็คเกจ `apt`
- ติดตั้ง: `openjdk-17-jdk`, `libgl1-mesa-dev`, `xz-utils` เป็นต้น
- เหมาะสำหรับ: เดสก์ท็อปลินุกซ์, WSL2, อินสแตนซ์บนคลาวด์

### **Fedora/RHEL/CentOS**
- ใช้ตัวจัดการแพ็คเกจ `dnf`
- ติดตั้ง: `java-17-openjdk-deep`, `libglvnd-glx`, `xz`, `lz4` เป็นต้น
- เหมาะสำหรับ: ระบบองค์กรที่ใช้เรดแฮท

### **Termux**
- ใช้ตัวจัดการแพ็คเกจ `pkg` (สภาพแวดล้อมเทอร์มินัลบน Android)
- ติดตั้ง: `openjdk-17`, เครื่องมือคำสั่ง Android
- เหมาะสำหรับ: การพัฒนา Flutter บนอุปกรณ์ Android โดยตรง
- หมายเหตุ: มีข้อจำกัดบางประการเมื่อเทียบกับลินุกซ์บนเดสก์ท็อป

### **Windows**
- แนะนำให้ติดตั้งด้วยตนเอง
- ทางเลือก: การติดตั้งบน Windows โดยตรง หรือใช้ WSL2 (แนะนำ)
- ต้องการ: การดาวน์โหลด Flutter SDK, Android Studio, JDK 17 ด้วยตนเอง
- แนวทางปฏิบัติที่ดีที่สุด: ใช้ WSL2 พร้อม Ubuntu เพื่อประสบการณ์แบบลินุกซ์

## 🚀 **ตัวอย่างการใช้งานอย่างรวดเร็ว**

### **บน Ubuntu/Debian/Kali:**
```bash
# ดาวน์โหลดและรันสคริปต์ติดตั้ง
wget https://raw.githubusercontent.com/your-repo/cyborg-dev/main/install_flutter_ubuntu.sh
chmod +x install_flutter_ubuntu.sh
./install_flutter_ubuntu.sh

# หลังจากการติดตั้งเสร็จสิ้น:
source ~/.bashrc
flutter doctor
flutter create my_cyborg_app
cd my_cyborg_app
flutter run  # เชื่อมต่ออุปกรณ์ Android หรือเริ่ม emulator ก่อน
```

### **บน Fedora:**
```bash
# ดาวน์โหลดและรันสคริปต์ติดตั้ง
wget https://raw.githubusercontent.com/your-repo/cyborg-dev/main/install_flutter_fedora.sh
chmod +x install_flutter_fedora.sh
./install_flutter_fedora.sh

# หลังจากการติดตั้งเสร็จสิ้น:
source ~/.bashrc
flutter doctor
```

### **บน Termux:**
```bash
# ดาวน์โหลดและรันสคริปต์ติดตั้ง
wget https://raw.githubusercontent.com/your-repo/cyborg-dev/main/install_flutter_termux.sh
chmod +x install_flutter_termux.sh
./install_flutter_termux.sh

# หลังจากการติดตั้งเสร็จสิ้น:
source ~/.bashrc
flutter doctor
```

### **บน Windows (แนะนำให้ใช้ WSL2):**
```powershell
# ใน PowerShell (ในฐานะผู้ดูแลระบบ):
wsl --install -d Ubuntu
# จากนั้นเปิด Ubuntu และรัน:
wget https://raw.githubusercontent.com/your-repo/cyborg-dev/main/install_flutter_ubuntu.sh
chmod +x install_flutter_ubuntu.sh
./install_flutter_ubuntu.sh
```

## 📁 **โครงสร้างไดเรกทอรีหลังการติดตั้ง**

หลังจากรันสคริปต์ติดตั้งใดๆ คุณจะได้โครงสร้างดังนี้:

```
$HOME/
├── android/
│   └── sdk/                    # Android SDK
│       ├── platform-tools/     # adb, fastboot
│       ├── cmdline-tools/      # SDK manager
│       └── platforms/          # แพลตฟอร์ม Android
├── development/
│   └── flutter/                # Flutter SDK
│       ├── bin/                # คำสั่ง flutter, dart
│       ├── packages/
│       └── ...
└── .bashrc                     // อัปเดตด้วย PATH และ ANDROID_SDK_ROOT
```

## 🔍 **การตรวจสอบและการแก้ไขปัญหา**

### **ตรวจสอบการติดตั้ง**
```bash
flutter --version
flutter doctor
flutter doctor --android-licenses  # ยอมรับใบอนุญาตหากจำเป็น
```

### **ปัญหาที่พบบ่อยและวิธีแก้ไข**

1. **"ไม่พบคำสั่ง: flutter"**
   - วิธีแก้: รีสตาร์ทเทอร์มินัลหรือรัน `source ~/.bashrc`
   - ตรวจสอบ: `echo $PATH` ควรมีไดเรกทอรี bin ของ Flutter

2. **"สถานะใบอนุญาต Android ไม่ทราบ"**
   - วิธีแก้: รัน `flutter doctor --android-licenses` และยอมรับทั้งหมดโดยพิมพ์ `y`

3. **"ไม่พบ Java"**
   - วิธีแก้: ตรวจสอบว่า `java -version` แสดงเวอร์ชัน 17.x
   - ตรวจสอบ: `echo $JAVA_HOME` ถูกตั้งค่าอย่างถูกต้อง

4. **"ไม่พบ Android SDK"**
   - วิธีแก้: ตรวจสอบว่า `echo $ANDROID_SDK_ROOT` ชี้ไปยังไดเรกทอรีที่ถูกต้อง
   - ตรวจสอบ: `$ANDROID_SDK_ROOT/platform-tools/adb` มีอยู่จริง

5. **ปัญหาประสิทธิภาพกับ Android Emulator**
   - วิธีแก้: เปิดใช้งานการเร่งความเร็วด้วยฮาร์ดแวร์ (HAXM บน Intel, Hyper-V บน AMD)
   - ทางเลือกอื่น: ใช้อุปกรณ์จริงผ่านการดีบัก USB

## 📚 **แหล่งข้อมูลและอ้างอิง**

- **เอกสารทางการของ Flutter**: https://flutter.dev/docs/get-started/install
- **เครื่องมือคำสั่ง Android SDK**: https://developer.android.com/studio/command-line
- **วิกิของ Flutter**: https://github.com/flutter/flutter/wiki
- **แรงบันดาลใจ**: https://github.com/mumumusuc/termux-flutter.git

## 🛡️ **หมายเหตุด้านความปลอดภัย**

- สคริปต์ทั้งหมดใช้แหล่งที่มาอย่างเป็นทางการ (Google, Flutter, Adoptium)
- ไม่มีการแจกจ่ายไบนารีที่ถูกดัดแปลงหรืออาจเป็นอันตราย
- สคริปต์สร้างไดเรกทอรีที่แยกจากกันในโฟลเดอร์บ้านของคุณ
- ตัวแปรสภาพแวดล้อมจะถูกเพิ่มเข้าไปใน `~/.bashrc` เท่านั้น
- คุณสามารถลบไดเรกทอรีการติดตั้งออกได้อย่างปลอดภัยหากจำเป็น

## 🎯 **คำแนะนำ**

1. **สำหรับลินุกซ์บนเดสก์ท็อป**: ใช้สคริปต์เฉพาะแพลตฟอร์ม (`install_flutter_ubuntu.sh` หรือ `install_flutter_fedora.sh`)
2. **สำหรับอุปกรณ์ Android**: ใช้สคริปต์ Termux (`install_flutter_termux.sh`)
3. **สำหรับ Windows**: ใช้ WSL2 พร้อมสคริปต์ Ubuntu เพื่อประสบการณ์ที่ดีที่สุด
4. **สำหรับสภาพแวดล้อมแบบผสม**: ใช้สคริปต์หลายแพลตฟอร์ม (`install_flutter_multiplatform.sh`)

## 🔄 **การอัปเดต Flutter**

เพื่ออัปเดต Flutter เป็นเวอร์ชันล่าสุด:
```bash
flutter upgrade
flutter doctor
```

เพื่ออัปเดตส่วนประกอบของ Android SDK:
```bash
sdkmanager --update
```

## ❓ **ต้องการความช่วยเหลือ?**

หากคุณพบปัญหา:
1. รัน `flutter doctor -v` เพื่อดูผลลัพธ์แบบละเอียด
2. ตรวจสอบคู่มือการแก้ไขปัญหาของ Flutter อย่างเป็นทางการ: https://flutter.dev/docs/get-started/troubleshoot
3. เยี่ยมชมชุมชน Flutter: https://flutter.dev/community
4. สำหรับปัญหาที่เกี่ยวข้องกับ Android โดยเฉพาะ: https://developer.android.com/studio/troubleshoot

---

**มีความสุขกับการพัฒนา Flutter!** 🎉

*คู่มือการติดตั้งนี้เป็นส่วนหนึ่งของโครงการ Cyborg Nexus และออกแบบมาเพื่อให้คุณเริ่มต้นการพัฒนา Flutter ได้อย่างรวดเร็วและน่าเชื่อถือบนทุกแพลตฟอร์มหลัก*