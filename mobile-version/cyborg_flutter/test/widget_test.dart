// This is a basic Flutter widget test for Cyborg Nexus.

import 'package:flutter_test/flutter_test.dart';
import 'package:cyborg_flutter/main.dart';

void main() {
  testWidgets('Cyborg Nexus home screen smoke test', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(const CyborgApp());

    // Verify that our app name is present.
    expect(find.text('CYBORG NEXUS'), findsOneWidget);

    // Verify that the initial engine response is present.
    expect(find.text('>> CYBORG ENGINE READY.'), findsOneWidget);
  });
}
