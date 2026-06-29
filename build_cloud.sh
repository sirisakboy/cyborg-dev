#!/bin/bash

# Cyborg Nexus Cloud Build Script
# This script automates the Go FFI and Flutter build process on Linux cloud environments.

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}==================================================${NC}"
echo -e "${BLUE}   CYBORG NEXUS CLOUD BUILD SYSTEM v1.0${NC}"
echo -e "${BLUE}==================================================${NC}"

# 1. Go Engine Build
echo -e "\n${GREEN}[1/3] Building Go Shared Library...${NC}"
cd mobile-version/tgpt-main
# Build for Linux (Shared Library)
go build -buildmode=c-shared -o libcyborg.so ffi_bridge.go
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Go shared library (libcyborg.so) created successfully.${NC}"
else
    echo -e "${RED}✗ Go build failed. Please ensure Go and GCC are installed.${NC}"
    exit 1
fi
cd ../..

# 2. Flutter Dependency Setup
echo -e "\n${GREEN}[2/3] Updating Flutter dependencies...${NC}"
cd mobile-version/cyborg_flutter
flutter pub get
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Flutter dependencies updated.${NC}"
else
    echo -e "${RED}✗ Flutter pub get failed.${NC}"
    exit 1
fi
cd ../..

# 3. Copy Go Lib to Flutter Project
echo -e "\n${GREEN}[3/3] Deploying Go Library to Flutter...${NC}"
# Correct path: mobile-version/cyborg_flutter/android/app/src/main/jniLibs/arm64-v8a
DEST_DIR="mobile-version/cyborg_flutter/android/app/src/main/jniLibs/arm64-v8a"
mkdir -p "$DEST_DIR"
cp mobile-version/tgpt-main/libcyborg.so "$DEST_DIR/"

# Also copy to Linux directory for Linux builds
mkdir -p mobile-version/cyborg_flutter/linux/
cp mobile-version/tgpt-main/libcyborg.so mobile-version/cyborg_flutter/linux/libcyborg.so

# Copy to web directory for web builds
mkdir -p mobile-version/cyborg_flutter/web/
cp mobile-version/tgpt-main/libcyborg.so mobile-version/cyborg_flutter/web/libcyborg.so

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Go library deployed to Flutter project.${NC}"
else
    echo -e "${RED}✗ Deployment failed.${NC}"
    exit 1
fi

echo -e "\n${BLUE}==================================================${NC}"
echo -e "${GREEN}BUILD SUCCESSFUL!${NC}"
echo -e "${BLUE}You can now run the app using 'flutter run' in the cyborg_flutter directory.${NC}"
echo -e "${BLUE}==================================================${NC}"