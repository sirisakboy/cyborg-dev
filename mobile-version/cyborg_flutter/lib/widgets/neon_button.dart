import 'package:flutter/material.dart';
import '../theme/app_theme.dart';

class NeonButton extends StatelessWidget {
  final String text;
  final VoidCallback onPressed;
  final Color color;

  const NeonButton({super.key, required this.text, required this.onPressed, this.color = CyborgTheme.neonBlue});

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        border: Border.all(color: color, width: 1),
      ),
      child: TextButton(
        onPressed: onPressed,
        style: TextButton.styleFrom(
          foregroundColor: color,
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
        ),
        child: Text(text, style: const TextStyle(fontFamily: 'Courier New', fontWeight: FontWeight.bold)),
      ),
    );
  }
}
