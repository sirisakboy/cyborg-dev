#!/bin/bash
# Flutter Installation Script for Termux

set -e

echo -e "\e[34m====================================\e[0m"
echo -e "\e[34m    Flutter Installation for Termux\e[0m"
echo -e "\e[34m====================================\e[0m"

# Update packages
echo -e "\e[33mUpdating Termux packages...\e[0m"
pkg update -y && pkg upgrade -y

# Install dependencies
echo -e "\e[33mInstalling dependencies...\e[0m"
pkg install -y curl git wget unzip zip liblz4 clang

# Install OpenJDK 17
echo -e "\e[33mInstalling OpenJDK 17...\e[0m"
pkg install -y openjdk-17

# Set up Android SDK (Termux already has some Android tools, but we'll set up Flutter-compatible ones)
echo -e "\e[33mSetting up Android development environment...\e[0m"
mkdir -p ~/android/sdk
ANDROID_SDK_ROOT="$HOME/android/sdk"
mkdir -p "$ANDROID_SDK_ROOT/cmdline-tools/latest"
cd ~/android

# Download Android command line tools
echo -e "\e[33mDownloading Android command line tools...\e[0m"
wget -q https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip
unzip -q commandlinetools-linux-9477386_latest.zip -d cmdline-tools
mv cmdline-tools/cmdline-tools/* cmdline-tools/latest/
rm -rf commandlinetools-linux-9477386_latest.zip

# Install SDK platforms
echo -e "\e[33mInstalling Android SDK platforms...\e[0m"
yes | $ANDROID_SDK_ROOT/cmdline-tools/latest/bin/sdkmanager --sdk_root=$ANDROID_SDK_ROOT --install "platforms;android-33" >/dev/null 2>&1
yes | $ANDROID_SDK_ROOT/cmdline-tools/latest/bin/sdkmanager --sdk_root=$ANDROID_SDK_ROOT --install "platform-tools" >/dev/null 2>&1
yes | $ANDROID_SDK_ROOT/cmdline-tools/latest/bin/sdkmanager --sdk_root=$ANDROID_SDK_ROOT --install "build-tools;33.0.2" >/dev/null 2>&1

# Set environment variables
echo -e "\e[33mSetting up environment variables...\e[0m"
echo "export ANDROID_SDK_ROOT=$ANDROID_SDK_ROOT" >> ~/.bashrc
echo 'export PATH=$PATH:$ANDROID_SDK_ROOT/platform-tools' >> ~/.bashrc
echo 'export PATH=$PATH:$ANDROID_SDK_ROOT/cmdline-tools/latest/bin' >> ~/.bashrc
source ~/.bashrc

# Install Flutter
echo -e "\e[33mInstalling Flutter...\e[0m"
git clone https://github.com/flutter/flutter.git ~/development/flutter
echo 'export PATH=$PATH:$HOME/development/flutter/bin' >> ~/.bashrc
source ~/.bashrc

# Verify installation
echo -e "\e[33mVerifying installation...\e[0m"
flutter --version
flutter doctor

echo -e "\e[32m====================================\e[0m"
echo -e "\e[32m  INSTALLATION COMPLETE!\e[0m"
echo -e "\e[32m====================================\e[0m"
echo -e "\e[32mFlutter: $HOME/development/flutter\e[0m"
echo -e "\e[32mAndroid SDK: $HOME/android/sdk\e[0m"
echo -e "\e[33mNext steps:\e[0m"
echo -e "\e[33m1. Restart your terminal session\e[0m"
echo -e "\e[33m2. Run 'flutter doctor' to verify setup\e[0m"
echo -e "\e[33m3. For Android development: flutter emulators\e[0m"
echo -e "\e[32m====================================\e[0m"