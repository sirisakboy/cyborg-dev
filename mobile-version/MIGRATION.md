# Cyborg Android Migration Plan (Flutter Path)

## 1. Analysis Summary
The current project (`main.py`) is a Python/Tkinter application acting as a GUI wrapper around various AI providers, including a `tgpt` CLI binary. 
Key functionalities to migrate to Android:
1.  **AI Engine:** The `tgpt` Go core (in `mobile-version/tgpt-main`) will be the primary engine.
2.  **Multimodal Features:** Vision (BUG_SCAN) and Image Generation.
3.  **UI/UX:** Needs to be ported from Tkinter to Flutter.
4.  **Local Storage:** Handling generated images and logs locally on Android.

## 2. Proposed Android Project Structure (`mobile-version/`)

```text
mobile-version/
├── tgpt-main/              # Existing Go core engine
└── cyborg_flutter/         # Flutter application project
    ├── android/            # Android-specific configuration
    ├── lib/                # Flutter UI code
    ├── pubspec.yaml        # Flutter dependencies
    └── ...
```

## 3. Migration Roadmap (Flutter Focused)

| Phase | Goal | Actions | Status |
| :--- | :--- | :--- | :--- |
| **P1** | **Project Setup** | Initialize `cyborg_flutter` and Gomobile setup. | ✅ In Progress |
| **P2** | **Go Integration** | Build Go library (`.so`) and bridge via FFI. | ⏳ |
| **P3** | **UI Porting** | Recreate Tkinter screens in Flutter. | ⏳ |
| **P4** | **Feature parity**| Integrate Vision API and Image Gen logic. | ⏳ |
| **P5** | **Testing** | Validate on Emulator/Device. | ⏳ |

## 4. Next Steps
1. Gomobile configuration to build Go core as a shared library.
2. Flutter-Go FFI implementation.
