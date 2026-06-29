#!/bin/bash

# Cyborg Nexus Multi-Platform Flutter & SDK Installation Script
# Supports: Ubuntu, Debian, Kali Linux, Fedora, Windows (WSL/WSL2), Termux
# Based on and inspired by: https://github.com/mumumusuc/termux-flutter.git

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}==================================================${NC}"
echo -e "${BLUE}   CYBORG NEXUS MULTI-PLATFORM FLUTTER INSTALLER${NC}"
echo -e "${BLUE}==================================================${NC}"

# Detect OS and distribution
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if [[ -f "/etc/os-release" ]]; then
            . /etc/os-release
            OS=$NAME
            VERSION=$VERSION_ID
        elif [[ -f "/etc/lsb-release" ]]; then
            . /etc/lsb-release
            OS=$DISTRIB_ID
            VERSION=$DISTRIB_RELEASE
        elif [[ -f "/etc/debian_version" ]]; then
            OS="Debian"
            VERSION=$(cat /etc/debian_version)
        elif [[ -f "/etc/redhat-release" ]]; then
            OS="Red Hat"
            VERSION=$(cat /etc/redhat-release)
        else
            OS=$(uname -s)
            VERSION=$(uname -r)
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macOS"
        VERSION=$(sw_vers -productVersion)
    elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
        OS="Windows"
        VERSION=$(cmd /c "ver")
    elif [[ "$OSTYPE" == "android"* ]] || [[ "$TERMUX_VERSION" != "" ]]; then
        OS="Termux"
        VERSION=$(getprop ro.build.version.release)
    else
        OS=$(uname -s)
        VERSION=$(uname -r)
    fi
    
    echo "$OS"
}

# Install dependencies based on OS
install_dependencies() {
    local os=$1
    
    case "$os" in
        "Ubuntu"|"Kali Linux"*)
            echo -e "${YELLOW}Installing dependencies for Ubuntu/Debian/Kali...${NC}"
            sudo apt update
            sudo apt install -y curl git wget unzip libgl1-mesa-dev xz-utils zip liblz4-tool
            ;;
        "Fedora"*)
            echo -e "${YELLOW}Installing dependencies for Fedora...${NC}"
            sudo dnf install -y curl git wget unzip which libglvnd-glx xz zip lz4
            ;;
        "Termux"*)
            echo -e "${YELLOW}Installing dependencies for Termux...${NC}"
            pkg update -y
            pkg install -y curl git wget unzip zip liblz4
            ;;
        "Windows"*)
            echo -e "${YELLOW}For Windows, please use PowerShell or WSL2.${NC}"
            echo -e "${YELLOW}Refer to the Windows-specific instructions below.${NC}"
            return 1
            ;;
        *)
            echo -e "${YELLOW}Unknown OS: $os. Attempting generic installation...${NC}"
            # Try common package managers
            if command -v apt-get &> /dev/null; then
                sudo apt-get update
                sudo apt-get install -y curl git wget unzip zip liblz4-tool
            elif command -v dnf &> /dev/null; then
                sudo dnf install -y curl git wget unzip zip lz4
            elif command -v pacman &> /dev/null; then
                sudo pacman -Sy --noconfirm curl git wget unzip zip lz4
            else
                echo -e "${RED}Could not determine package manager. Please install dependencies manually.${NC}"
                return 1
            fi
            ;;
    esac
}

# Install Java (required for Android development)
install_java() {
    local os=$1
    
    echo -e "${YELLOW}Installing OpenJDK 17 (required for Android development)...${NC}"
    
    case "$os" in
        "Ubuntu"|"Kali Linux"*)
            sudo apt install -y openjdk-17-jdk
            ;;
        "Fedora"*)
            sudo dnf install -y java-17-openjdk-devel
            ;;
        "Termux"*)
            pkg install -y openjdk-17
            ;;
        "Windows"*)
            echo -e "${YELLOW}For Windows, please install JDK 17 manually from: https://adoptium.net/${NC}"
            return 1
            ;;
        *)
            if command -v apt-get &> /dev/null; then
                sudo apt-get install -y openjdk-17-jdk
            elif command -v dnf &> /dev/null; then
                sudo dnf install -y java-17-openjdk-devel
            else
                echo -e "${YELLOW}Please install OpenJDK 17 manually for your system.${NC}"
                return 1
            fi
            ;;
    esac
}

# Install Android Studio command line tools
install_android_tools() {
    local install_dir=$1
    
    echo -e "${YELLOW}Installing Android SDK command line tools...${NC}"
    
    # Create Android directory
    mkdir -p "$install_dir/android"
    ANDROID_SDK_ROOT="$install_dir/android/sdk"
    mkdir -p "$ANDROID_SDK_ROOT"
    
    # Download and install command line tools
    cd "$install_dir"
    if [[ "$OSTYPE" == "linux-gnu"* ]] || [[ "$OSTYPE" == "android"* ]] || [[ "$TERMUX_VERSION" != "" ]]; then
        wget -q https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip -o cmdline-tools.zip
    else
        echo -e "${YELLOW}Please download Android command line tools manually for your platform.${NC}"
        return 1
    fi
    
    unzip -q cmdline-tools.zip
    mkdir -p "$ANDROID_SDK_ROOT/cmdline-tools/latest"
    mv cmdline-tools/* "$ANDROID_SDK_ROOT/cmdline-tools/latest/"
    rm -rf cmdline-tools cmdline-tools.zip
    
    # Install SDK platforms and tools
    echo -e "${YELLOW}Installing Android SDK platforms and tools...${NC}"
    yes | "$ANDROID_SDK_ROOT/cmdline-tools/latest/bin/sdkmanager" --sdk_root="$ANDROID_SDK_ROOT" --install "platforms;android-33" >/dev/null 2>&1
    yes | "$ANDROID_SDK_ROOT/cmdline-tools/latest/bin/sdkmanager" --sdk_root="$ANDROID_SDK_ROOT" --install "platform-tools" >/dev/null 2>&1
    yes | "$ANDROID_SDK_ROOT/cmdline-tools/latest/bin/sdkmanager" --sdk_root="$ANDROID_SDK_ROOT" --install "build-tools;33.0.2" >/dev/null 2>&1
    
    # Set up environment variables
    echo "export ANDROID_SDK_ROOT=$ANDROID_SDK_ROOT" >> "$HOME/.bashrc"
    echo 'export PATH=$PATH:$ANDROID_SDK_ROOT/platform-tools' >> "$HOME/.bashrc"
    echo 'export PATH=$PATH:$ANDROID_SDK_ROOT/cmdline-tools/latest/bin' >> "$HOME/.bashrc"
    
    # Source the bashrc to make changes available in current session
    source "$HOME/.bashrc"
    
    echo -e "${GREEN}Android SDK installed successfully!${NC}"
}

# Install Flutter
install_flutter() {
    local install_dir=$1
    
    echo -e "${YELLOW}Installing Flutter...${NC}"
    
    # Create development directory
    mkdir -p "$install_dir/development"
    FLUTTER_ROOT="$install_dir/development/flutter"
    
    # Clone Flutter repository
    git clone https://github.com/flutter/flutter.git "$FLUTTER_ROOT"
    
    # Add Flutter to PATH
    echo "export PATH=\$PATH:$FLUTTER_ROOT/bin" >> "$HOME/.bashrc"
    source "$HOME/.bashrc"
    
    # Run flutter doctor to verify installation
    echo -e "${YELLOW}Running Flutter doctor to verify installation...${NC}"
    "$FLUTTER_ROOT/bin/flutter" doctor --android-licenses
    
    echo -e "${GREEN}Flutter installed successfully!${NC}"
}

# Install VS Code (optional but recommended)
install_vscode() {
    local os=$1
    
    echo -e "${YELLOW}Installing Visual Studio Code (recommended for Flutter development)...${NC}"
    
    case "$os" in
        "Ubuntu"|"Kali Linux"*)
            wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
            sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
            sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
            rm -f packages.microsoft.gpg
            sudo apt update
            sudo apt install -y code
            ;;
        "Fedora"*)
            sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
            sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
            sudo dnf check-update
            sudo dnf install -y code
            ;;
        "Termux"*)
            echo -e "${YELLOW}For Termux, consider using a terminal-based editor like vim or nano instead.${NC}"
            return 1
            ;;
        "Windows"*)
            echo -e "${YELLOW}For Windows, please download VS Code from: https://code.visualstudio.com/${NC}"
            return 1
            ;;
        *)
            if command -v apt-get &> /dev/null; then
                wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
                sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
                sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
                rm -f packages.microsoft.gpg
                sudo apt update
                sudo apt install -y code
            elif command -v dnf &> /dev/null; then
                sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
                sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
                sudo dnf check-update
                sudo dnf install -y code
            else
                echo -e "${YELLOW}Please install Visual Studio Code manually for your system.${NC}"
                return 1
            fi
            ;;
    esac
}

# Main installation function
main_installation() {
    # Detect OS
    OS=$(detect_os)
    echo -e "${GREEN}Detected OS: $OS${NC}"
    
    # Set installation directory (default to home directory)
    INSTALL_DIR="$HOME/cyborg-dev-tools"
    mkdir -p "$INSTALL_DIR"
    
    echo -e "${YELLOW}Installation directory: $INSTALL_DIR${NC}"
    
    # Install dependencies
    if ! install_dependencies "$OS"; then
        echo -e "${RED}Failed to install dependencies.${NC}"
        return 1
    fi
    
    # Install Java
    if ! install_java "$OS"; then
        echo -e "${RED}Failed to install Java.${NC}"
        return 1
    fi
    
    # Install Android tools
    if ! install_android_tools "$INSTALL_DIR"; then
        echo -e "${RED}Failed to install Android tools.${NC}"
        return 1
    fi
    
    # Install Flutter
    if ! install_flutter "$INSTALL_DIR"; then
        echo -e "${RED}Failed to install Flutter.${NC}"
        return 1
    fi
    
    # Install VS Code (optional)
    install_vscode "$OS"
    
    # Final verification
    echo -e "${YELLOW}Running final verification...${NC}"
    flutter --version
    flutter doctor
    
    echo -e "${BLUE}==================================================${NC}"
    echo -e "${GREEN}INSTALLATION COMPLETE!${NC}"
    echo -e "${BLUE}==================================================${NC}"
    echo -e "${GREEN}Flutter SDK: $FLUTTER_ROOT${NC}"
    echo -e "${GREEN}Android SDK: $ANDROID_SDK_ROOT${NC}"
    echo -e "${BLUE}==================================================${NC}"
    echo -e "${YELLOW}Next steps:${NC}"
    echo -e "${YELLOW}1. Restart your terminal or run: source ~/.bashrc${NC}"
    echo -e "${YELLOW}2. Run 'flutter doctor' to verify your setup${NC}"
    echo -e "${YELLOW}3. For Android development, connect a device or start an emulator${NC}"
    echo -e "${YELLOW}4. To create a new Flutter project: flutter create my_app${NC}"
    echo -e "${BLUE}==================================================${NC}"
}

# Windows-specific instructions
show_windows_instructions() {
    echo -e "${BLUE}==================================================${NC}"
    echo -e "${BLUE}   WINDOWS SPECIFIC INSTRUCTIONS${NC}"
    echo -e "${BLUE}==================================================${NC}"
    echo -e "${YELLOW}For Windows, we recommend using WSL2 (Windows Subsystem for Linux)${NC}"
    echo -e "${YELLOW}for the best Flutter development experience.${NC}"
    echo -e ""
    echo -e "${YELLOW}To install Flutter on Windows natively:${NC}"
    echo -e "${YELLOW}1. Download Flutter SDK from: https://storage.googleapis.com/flutter_infra_release/flutter/windows/${NC}"
    echo -e "${YELLOW}2. Extract the zip file to a location like C:\\src\\flutter${NC}"
    echo -e "${YELLOW}3. Update your PATH to include C:\\src\\flutter\\bin${NC}"
    echo -e "${YELLOW}4. Download and install Android Studio from: https://developer.android.com/studio${NC}"
    echo -e "${YELLOW}5. Install JDK 17 from: https://adoptium.net/${NC}"
    echo -e "${YELLOW}6. Run 'flutter doctor' to verify setup${NC}"
    echo -e ""
    echo -e "${YELLOW}To use WSL2 (Recommended):${NC}"
    echo -e "${YELLOW}1. Enable WSL2: wsl --install${NC}"
    echo -e "${YELLOW}2. Install Ubuntu from Microsoft Store${NC}"
    echo -e "${YELLOW}3. Run this script inside the Ubuntu WSL2 terminal${NC}"
    echo -e "${BLUE}==================================================${NC}"
}

# Main script execution
echo -e "${BLUE}Starting Flutter multi-platform installation...${NC}"

OS=$(detect_os)

if [[ "$OS" == "Windows"* ]]; then
    show_windows_instructions
    echo -e "${YELLOW}Would you like to continue with WSL2/Linux-style installation? (y/n):${NC}"
    read -r response
    if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
        # Continue with Linux-style installation (assuming WSL2)
        main_installation
    else
        echo -e "${YELLOW}Please follow the Windows-specific instructions above.${NC}"
        exit 0
    fi
else
    main_installation
fi