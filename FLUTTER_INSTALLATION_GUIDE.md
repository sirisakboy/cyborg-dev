# Cyborg Nexus Flutter Installation Guide

This guide provides multiple options for installing Flutter and Android SDK across different platforms. Choose the method that best fits your operating system and preferences.

## 📋 **Available Installation Methods**

### 1. **Universal Multi-Platform Script** (Recommended for most Linux systems)
```bash
./install_flutter_multiplatform.sh
```
- **Supports**: Ubuntu, Debian, Kali Linux, Fedora, Termux
- **Features**: Auto-detects OS, installs all dependencies, sets up Flutter + Android SDK
- **Based on**: Principles from https://github.com/mumumusuc/termux-flutter.git

### 2. **Platform-Specific Scripts**
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

### 3. **Windows Installation**
Refer to: `install_flutter_windows.md` for detailed manual instructions

## 🔧 **What Gets Installed**

All installation methods will set up:

### ✅ **Core Components**
- **Flutter SDK** (latest stable version from official repository)
- **Android SDK** with:
  - Platform Tools (adb, fastboot)
  - Build Tools (version 33.0.2)
  - Android Platform (API 33 - Android 13.0)
- **OpenJDK 17** (required for Android development)
- **Essential Tools**: git, wget, unzip, zip, clang

### ✅ **Environment Configuration**
- Automatic setup of `ANDROID_SDK_ROOT` environment variable
- Automatic addition of Flutter and Android platform-tools to `PATH`
- Persistent configuration via `~/.bashrc` (or equivalent)

### ✅ **Verification**
- Automatic `flutter --version` and `flutter doctor` checks
- Android license acceptance prompts

## 🖥️ **Platform-Specific Details**

### **Ubuntu/Debian/Kali Linux**
- Uses `apt` package manager
- Installs: `openjdk-17-jdk`, `libgl1-mesa-dev`, `xz-utils`, etc.
- Ideal for: Desktop Linux, WSL2, cloud instances

### **Fedora/RHEL/CentOS**
- Uses `dnf` package manager  
- Installs: `java-17-openjdk-devel`, `libglvnd-glx`, `xz`, `lz4`, etc.
- Ideal for: Red Hat-based enterprise systems

### **Termux**
- Uses `pkg` package manager (Android terminal environment)
- Installs: `openjdk-17`, Android command line tools
- Ideal for: Flutter development directly on Android devices
- Note: Some limitations apply compared to desktop Linux

### **Windows**
- Manual installation recommended
- Options: Native Windows installation or WSL2 (recommended)
- Requires: Manual download of Flutter SDK, Android Studio, JDK 17
- Best practice: Use WSL2 with Ubuntu for Linux-like experience

## 🚀 **Quick Start Examples**

### **On Ubuntu/Debian/Kali:**
```bash
# Download and run the installer
wget https://raw.githubusercontent.com/your-repo/cyborg-dev/main/install_flutter_ubuntu.sh
chmod +x install_flutter_ubuntu.sh
./install_flutter_ubuntu.sh

# After installation completes:
source ~/.bashrc
flutter doctor
flutter create my_cyborg_app
cd my_cyborg_app
flutter run  # Connect Android device or start emulator first
```

### **On Fedora:**
```bash
# Download and run the installer
wget https://raw.githubusercontent.com/your-repo/cyborg-dev/main/install_flutter_fedora.sh
chmod +x install_flutter_fedora.sh
./install_flutter_fedora.sh

# After installation completes:
source ~/.bashrc
flutter doctor
```

### **On Termux:**
```bash
# Download and run the installer
wget https://raw.githubusercontent.com/your-repo/cyborg-dev/main/install_flutter_termux.sh
chmod +x install_flutter_termux.sh
./install_flutter_termux.sh

# After installation completes:
source ~/.bashrc
flutter doctor
```

### **On Windows (WSL2 Recommended):**
```powershell
# In PowerShell (Admin):
wsl --install -d Ubuntu
# Then launch Ubuntu and run:
wget https://raw.githubusercontent.com/your-repo/cyborg-dev/main/install_flutter_ubuntu.sh
chmod +x install_flutter_ubuntu.sh
./install_flutter_ubuntu.sh
```

## 📁 **Directory Structure After Installation**

After running any of the installation scripts, you'll have:

```
$HOME/
├── android/
│   └── sdk/                    # Android SDK
│       ├── platform-tools/     # adb, fastboot
│       ├── cmdline-tools/      # SDK manager
│       └── platforms/          # Android platforms
├── development/
│   └── flutter/                # Flutter SDK
│       ├── bin/                # flutter, dart commands
│       ├── packages/
│       └── ...
└── .bashrc                     # Updated with PATH and ANDROID_SDK_ROOT
```

## 🔍 **Verification & Troubleshooting**

### **Verify Installation**
```bash
flutter --version
flutter doctor
flutter doctor --android-licenses  # Accept licenses if needed
```

### **Common Issues & Solutions**

1. **"Command not found: flutter"**
   - Solution: Restart terminal or run `source ~/.bashrc`
   - Check: `echo $PATH` should contain Flutter bin directory

2. **"Android license status unknown"**
   - Solution: Run `flutter doctor --android-licenses` and accept all

3. **"Java not found"**
   - Solution: Verify `java -version` shows 17.x
   - Check: `echo $JAVA_HOME` is set correctly

4. **"Android SDK not found"**
   - Solution: Verify `echo $ANDROID_SDK_ROOT` points to correct directory
   - Check: `$ANDROID_SDK_ROOT/platform-tools/adb` exists

5. **Performance issues with Android Emulator**
   - Solution: Enable hardware acceleration (HAXM on Intel, Hyper-V on AMD)
   - Alternative: Use physical device via USB debugging

## 📚 **Resources & References**

- **Official Flutter Docs**: https://flutter.dev/docs/get-started/install
- **Android SDK Command Line Tools**: https://developer.android.com/studio/command-line
- **Flutter Wiki**: https://github.com/flutter/flutter/wiki
- **Inspiration**: https://github.com/mumumusuc/termux-flutter.git

## 🛡️ **Safety Notes**

- All scripts use official sources (Google, Flutter, Adoptium)
- No modified or potentially unsafe binaries are distributed
- Scripts create isolated directories in your home folder
- Environment variables are added to `~/.bashrc` only
- You can safely remove the installation directories if needed

## 🎯 **Recommendations**

1. **For Desktop Linux**: Use the platform-specific script (`install_flutter_ubuntu.sh` or `install_flutter_fedora.sh`)
2. **For Android Devices**: Use the Termux script (`install_flutter_termux.sh`)
3. **For Windows**: Use WSL2 with the Ubuntu script for best experience
4. **For Mixed Environments**: Use the multi-platform script (`install_flutter_multiplatform.sh`)

## 🔄 **Updating Flutter**

To update Flutter to the latest version:
```bash
flutter upgrade
flutter doctor
```

To update Android SDK components:
```bash
sdkmanager --update
```

## ❓ **Need Help?**

If you encounter issues:
1. Run `flutter doctor -v` for verbose output
2. Check the official Flutter troubleshooting guide: https://flutter.dev/docs/get-started/troubleshoot
3. Visit Flutter community: https://flutter.dev/community
4. For Android-specific issues: https://developer.android.com/studio/troubleshoot

---

**Happy Flutter Development!** 🎉

*This installation guide is part of the Cyborg Nexus project and is designed to get you up and running with Flutter development quickly and reliably across all major platforms.*