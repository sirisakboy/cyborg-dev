import 'package:flutter/material.dart';
import '../services/ffi_service.dart';

class CyborgController extends ChangeNotifier {
  final FfiService _ffiService = FfiService();
  String _response = ">> CYBORG ENGINE READY.";
  bool _isLoading = false;

  String get response => _response;
  bool get isLoading => _isLoading;
  bool get isEngineLoaded => _ffiService.isLoaded;

  Future<void> executeCommand(String prompt, String mode) async {
    _isLoading = true;
    _response = ">> PROCESSING $mode: $prompt...";
    notifyListeners();

    // Small delay for UI update
    await Future.delayed(const Duration(milliseconds: 300));

    try {
      if (_ffiService.isLoaded) {
        _response = _ffiService.executeCommand(prompt);
      } else {
        _response = ">> FFI Engine not loaded. Fallback/Mock:\n\nMock Result for: $prompt";
      }
    } catch (e) {
      _response = ">> ERROR calling FFI engine: $e";
    }

    _isLoading = false;
    notifyListeners();
  }
}
