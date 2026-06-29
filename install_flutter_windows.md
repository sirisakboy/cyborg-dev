# Flutter Installation Guide for Windows

## Prerequisites
- Windows 10 version 1903 or higher (or Windows 11)
- Administrator access to install software
- Minimum 4 GB RAM (8 GB recommended)
- 4 GB of free disk space (more for Android SDK/emulator)

## Installation Steps

### 1. Install Chocolatey (Package Manager - Optional but Recommended)
Open PowerShell as Administrator and run:
```powershell
Set-ExecutionPolicy Bypass -Scope Process -ExecutionPolicy Bypass
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

### 2. Install Required Dependencies
Using Chocolatey (recommended):
```powershell
choco install -y git jdk17 androidstudio android-sdk-platform-tools
```

Or manually install:
- **Git**: https://git-scm.com/download/win
- **JDK 17**: https://adoptium.net/temurin17/
- **Android Studio**: https://developer.android.com/studio

### 3. Download and Install Flutter SDK
1. Download the Flutter SDK zip file from: https://storage.googleapis.com/flutter_infra_release/flutter/windows/flutter_windows_3.24.3-stable.zip
2. Extract the zip file to a location like `C:\src\flutter` (avoid paths with spaces)
3. Add Flutter to your PATH:
   - Press `Win + R`, type `sysdm.cpl`, press Enter
   - Go to Advanced → Environment Variables
   - Under System Variables, find `Path`, click Edit
   - Click New and add `C:\src\flutter\bin`
   - Click OK on all dialogs

### 4. Set Up Android Development
1. Launch Android Studio (it should have been installed in step 2)
2. Go to Configure → SDK Manager
3. Under SDK Platforms tab, check "Show Package Details"
4. Select Android 13.0 (API 33)
5. Click Apply to install
6. Under SDK Tools tab, check:
   - Android SDK Platform-Tools
   - Android SDK Build-Tools (latest version)
   - Android Emulator (if you want to use emulator)
7. Click Apply to install

### 8. Set Environment Variables for Android
Add these to your System PATH:
- `%ANDROID_HOME%\platform-tools` (usually `C:\Users\<username>\AppData\Local\Android\Sdk\platform-tools`)
- `%ANDROID_HOME%\cmdline-tools\latest\bin` (if using command line tools)

### 9. Verify Installation
Open a new Command Prompt or PowerShell window and run:
```powershell
flutter --version
flutter doctor
```

### 10. Optional: Install Visual Studio Code
Download from: https://code.visualstudio.com/
- Install the Flutter and Dart extensions from the VS Code marketplace

## Troubleshooting

### Common Issues:
1. **"Android license status unknown"**
   - Run: `flutter doctor --android-licenses`
   - Accept all licenses by typing `y`

2. **"Flutter requires Android SDK"**
   - Ensure ANDROID_HOME or ANDROID_SDK_ROOT is set correctly
   - Verify platform-tools directory exists in your Android SDK path

3. **"Java not found"**
   - Ensure JDK 17 is installed and JAVA_HOME is set correctly
   - Verify `java -version` shows version 17.x

## Alternative: Using WSL2 (Recommended for Best Experience)
For the best Flutter development experience on Windows, consider using WSL2:

1. Enable WSL2: Open PowerShell as Admin and run `wsl --install`
2. Install Ubuntu from Microsoft Store
3. Launch Ubuntu and run the Linux installation script:
   ```bash
   bash <(curl -s https://raw.githubusercontent.com/your-repo/cyborg-dev/main/install_flutter_ubuntu.sh)
   ```

## Directory Structure After Installation
```
C:\
└── src\
    └── flutter\                # Flutter SDK
    └── android-sdk\            # Android SDK (if installed separately)
        ├── platform-tools\
        ├── cmdline-tools\
        └── platforms\
```

## Useful Commands
- `flutter doctor` - Check your Flutter setup
- `flutter devices` - List connected devices
- `flutter emulators` - List and manage Android emulators
- `flutter create my_app` - Create a new Flutter project
- `flutter run` - Run your app on a connected device