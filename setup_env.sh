#!/bin/bash

# Cyborg Nexus Environment Bootstrap Script
# This script installs Flutter SDK on GitHub Codespaces / Ubuntu Linux

echo "🚀 Starting Environment Setup..."

# 1. Install dependencies for Flutter
sudo apt-get update
sudo apt-get install -y curl git unzip xz-utils zip libglu1-mesa -y

# 2. Download Flutter SDK (Stable channel)
# Using a mirror or official source
FLUTTER_VERSION="3.22.0" # You can update this to the latest
FLUTTER_STORAGE_BASE_URL="https://storage.googleapis.com/flutter_infra_release/releases/stable"
FLUTTER_SAMPLED_VERSION="3.22.0"

echo "📦 Downloading Flutter SDK..."
git clone https://github.com/flutter/flutter.git -b stable ~/flutter

# 3. Add Flutter to PATH (current session and permanent)
echo 'export PATH="$PATH:$HOME/flutter/bin"' >> ~/.bashrc
export PATH="$PATH:$HOME/flutter/bin"

# 4. Pre-download Flutter artifacts
echo "⚙️ Configuring Flutter..."
flutter doctor

echo "✅ Flutter installed successfully!"
echo "⚠️ Please run 'source ~/.bashrc' to apply PATH changes to your current terminal."
echo "👉 Now you can run './build_cloud.sh' again."
