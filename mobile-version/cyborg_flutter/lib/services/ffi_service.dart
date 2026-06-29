import 'dart:ffi' as ffi;
import 'package:ffi/ffi.dart';
import 'dart:io' show Platform;
import 'package:flutter/foundation.dart' show debugPrint;

typedef ExecuteCommandC = ffi.Pointer<Utf8> Function(ffi.Pointer<Utf8> command);
typedef ExecuteCommandDart = ffi.Pointer<Utf8> Function(ffi.Pointer<Utf8> command);

typedef FreeStringC = ffi.Void Function(ffi.Pointer<Utf8> str);
typedef FreeStringDart = void Function(ffi.Pointer<Utf8> str);

class FfiService {
  late ffi.DynamicLibrary _lib;
  late ExecuteCommandDart _executeCommand;
  late FreeStringDart _freeString;
  bool _isLoaded = false;

  bool get isLoaded => _isLoaded;

  FfiService() {
    try {
      _loadLibrary();
      _isLoaded = true;
    } catch (e) {
      debugPrint("FFI Library load failed: $e");
    }
  }

  void _loadLibrary() {
    if (Platform.isAndroid) {
      _lib = ffi.DynamicLibrary.open('libcyborg.so');
    } else if (Platform.isWindows) {
      // Look for the dll in the build directory or local path
      _lib = ffi.DynamicLibrary.open('libcyborg.dll');
    } else if (Platform.isLinux) {
      _lib = ffi.DynamicLibrary.open('libcyborg.so');
    } else if (Platform.isMacOS) {
      _lib = ffi.DynamicLibrary.open('libcyborg.dylib');
    } else {
      // For web and other unsupported platforms, don't load the library
      _isLoaded = false;
      return;
    }

    try {
      _executeCommand = _lib
          .lookup<ffi.NativeFunction<ExecuteCommandC>>('ExecuteCommand')
          .asFunction<ExecuteCommandDart>();

      _freeString = _lib
          .lookup<ffi.NativeFunction<FreeStringC>>('FreeString')
          .asFunction<FreeStringDart>();
      _isLoaded = true;
    } catch (e) {
      _isLoaded = false;
      debugPrint('FFI Library load failed: $e');
    }
  }

  String executeCommand(String command) {
    if (!_isLoaded) {
      return "FFI Engine not loaded. Execute build first.";
    }
    
    final cmdPointer = command.toNativeUtf8();
    final resultPointer = _executeCommand(cmdPointer);
    
    final result = resultPointer.toDartString();
    
    malloc.free(cmdPointer);
    _freeString(resultPointer); // Safe memory release via Go runtime
    
    return result;
  }
}
