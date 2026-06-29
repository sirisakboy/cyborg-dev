import 'package:flutter/material.dart';
import 'theme/app_theme.dart';
import 'screens/cyborg_home_screen.dart';

void main() {
  runApp(const CyborgApp());
}

class CyborgApp extends StatelessWidget {
  const CyborgApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Cyborg Nexus',
      theme: CyborgTheme.darkTheme,
      home: const CyborgHomeScreen(),
    );
  }
}
