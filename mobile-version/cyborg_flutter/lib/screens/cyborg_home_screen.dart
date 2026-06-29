import 'package:flutter/material.dart';
import '../theme/app_theme.dart';
import '../controller/cyborg_controller.dart';
import '../widgets/neon_button.dart';

class CyborgHomeScreen extends StatefulWidget {
  const CyborgHomeScreen({super.key});

  @override
  State<CyborgHomeScreen> createState() => _CyborgHomeScreenState();
}

class _CyborgHomeScreenState extends State<CyborgHomeScreen> {
  final CyborgController _controller = CyborgController();
  final TextEditingController _promptController = TextEditingController();

  @override
  void initState() {
    super.initState();
    _controller.addListener(() => setState(() {}));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("CYBORG NEXUS", style: TextStyle(color: CyborgTheme.neonBlue)),
        backgroundColor: CyborgTheme.bgPanel,
      ),
      body: Column(
        children: [
          Expanded(
            child: Container(
              padding: const EdgeInsets.all(16),
              color: CyborgTheme.bgPanel,
              child: Text(_controller.response),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: TextField(
              controller: _promptController,
              style: const TextStyle(color: CyborgTheme.textWhite),
              decoration: const InputDecoration(
                hintText: "Enter Command...",
                hintStyle: TextStyle(color: CyborgTheme.bgPanel),
                border: OutlineInputBorder(),
                enabledBorder: OutlineInputBorder(borderSide: BorderSide(color: CyborgTheme.neonBlue)),
              ),
            ),
          ),
          if (_controller.isLoading) const LinearProgressIndicator(color: CyborgTheme.neonGreen),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              NeonButton(text: "⚡ EXEC", onPressed: () => _controller.executeCommand(_promptController.text, "CODE")),
              NeonButton(text: "🧹 CLEAN", onPressed: () {}, color: CyborgTheme.neonRed),
            ],
          ),
          const SizedBox(height: 20),
        ],
      ),
    );
  }
}
