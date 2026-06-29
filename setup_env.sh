#!/bin/bash

# Cyborg Nexus Ultra-Fast Flutter Setup
# Optimized for GitHub Codespaces / Linux Cloud

echo "⚡ FAST-TRACKING FLUTTER SETUP..."

# 1. Install minimal essential dependencies
sudo apt-get update -y && sudo apt-get install -y curl git unzip xz-utils zip libglu1-mesa

# 2. Ultra-fast Shallow Clone (only latest commit)
echo "📦 Downloading Flutter (Shallow Clone)..."
if [ ! -d "$HOME/flutter" ]; then
    git clone --depth 1 -b stable https://github.com/flutter/flutter.git ~/flutter
else
    echo "Flutter already exists, skipping download."
fi

# 3. Instant PATH Update
export PATH="$PATH:$HOME/flutter/bin"
echo 'export PATH="$PATH:$HOME/flutter/bin"' >> ~/.bashrc

# 4. Optimized Artifact Download
echo "⚙️ Pre-caching binaries for current platform..."
flutter precache

# 5. Final Health Check
flutter doctor -v | grep "Flutter"

echo -e "
✅ SETUP COMPLETE!"
echo -e "👉 Now run: source ~/.bashrc && ./build_cloud.sh"
