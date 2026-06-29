# Cyborg Nexus: Cross-Platform Build Plan

This document outlines the strategy for building the Cyborg Nexus application across multiple platforms (Android, iOS, Desktop, Web), bridging the Flutter UI with the Go core engine.

## 1. Core Architecture
- **UI:** Flutter (Dart).
- **Logic:** Go Engine (`tgpt-main/src`).
- **Communication Bridge:** FFI (Foreign Function Interface) using `dart:ffi`.

## 2. Platform-Specific Build Strategy

| Platform | Bridge Technique | Go Build Target |
| :--- | :--- | :--- |
| **Android** | `dart:ffi` / JNI | `c-shared` (`.so`) |
| **iOS** | `dart:ffi` | `c-archive` (`.a`) |
| **Windows** | `dart:ffi` | `c-shared` (`.dll`) |
| **macOS** | `dart:ffi` | `c-shared` (`.dylib`) |
| **Linux** | `dart:ffi` | `c-shared` (`.so`) |
| **Web** | WebAssembly (Wasm) | `js` / `wasm` |

## 3. Go Library Build Workflow
To expose Go functions to Flutter, use the following approach:

1. **Define C-Header:**
   ```go
   // Go: export MyFunction
   func MyFunction() { ... }
   ```
2. **Build Library (Example for Android/Linux):**
   ```bash
   go build -buildmode=c-shared -o libcyborg.so ./src/main.go
   ```
3. **Flutter FFI Binding:** 
   Use `ffigen` to generate Dart bindings automatically from the C-header file.

## 4. Cross-Platform Build Commands
- **Android:** `flutter build apk`
- **iOS:** `flutter build ios`
- **Windows:** `flutter build windows`
- **Web:** `flutter build web`
- **Automation:** Use `Makefile` to consolidate Go build + Flutter build steps.
