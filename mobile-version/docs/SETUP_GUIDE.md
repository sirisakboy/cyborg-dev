# Cyborg Nexus: Environment Setup & Icon Guide

## 1. Verify Go Installation
1. Open a **new** Terminal (important to refresh environment variables).
2. Run:
   ```bash
   go version
   ```
   *Expected: `go version go1.26.4 windows/amd64` (or similar).*

## 2. Setting Up App Icon (Flutter)
1. **Move Icon:** Move `cyborg_nexus_icon.png` (from project root) to `cyborg_flutter/assets/icon.png`. (Create `assets` folder if it doesn't exist).
2. **Add Dependency:** Open `cyborg_flutter/pubspec.yaml` and add:
   ```yaml
   dev_dependencies:
     flutter_launcher_icons: "^0.13.1"

   flutter_launcher_icons:
     image_path: "assets/icon.png"
     android: true
     ios: true
   ```
3. **Generate Icons:** Run:
   ```bash
   cd cyborg_flutter
   flutter pub get
   flutter pub run flutter_launcher_icons
   ```

## 3. Preparing for Go-FFI Integration
Now that Go is installed, the next step is building the bridge.
1. Ensure your `main.go` inside `tgpt-main` has a C-header import:
   ```go
   import "C"
   ```
2. You are now ready to build the shared library!
   ```bash
   go build -buildmode=c-shared -o libcyborg.so ./src/main.go
   ```
*(Note: For Windows, ensure you build for the correct architecture, e.g., using `gcc` via MinGW if needed.)*
