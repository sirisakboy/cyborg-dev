import 'package:flutter/material.dart';

class CyborgTheme {
  static const Color bgDark = Color(0xFF0A0F14);
  static const Color bgPanel = Color(0xFF101820);
  static const Color neonBlue = Color(0xFF00F0FF);
  static const Color neonRed = Color(0xFFFF0055);
  static const Color neonGreen = Color(0xFF39FF14);
  static const Color neonYellow = Color(0xFFFFCC00);
  static const Color textWhite = Color(0xFFE2E8F0);

  static ThemeData get darkTheme {
    return ThemeData(
      brightness: Brightness.dark,
      primaryColor: neonBlue,
      scaffoldBackgroundColor: bgDark,
      colorScheme: const ColorScheme.dark(
        primary: neonBlue,
        secondary: neonBlue,
        surface: bgPanel,
        background: bgDark,
      ),
      textTheme: const TextTheme(
        bodyMedium: TextStyle(color: textWhite, fontFamily: 'Courier New'),
      ),
    );
  }
}
