# Cyborg Nexus: Mobile UI Design

## 1. Design Concept
- **Theme:** "Dark Cybernetic".
- **Color Palette:**
  - Background: `#0A0F14`
  - Surface/Panel: `#101820`
  - Accent Blue: `#00F0FF` (Primary)
  - Accent Red: `#FF0055` (Alert/Clean)
  - Accent Green: `#39FF14` (Success/Action)
  - Accent Yellow: `#FFCC00` (Warning/Special)
  - Text: `#E2E8F0`

## 2. Layout Structure
- **Screen:** `CyborgHomeScreen`
  - **Header:** Provider Dropdown + App Title.
  - **Main Content:** `OutputArea` (ScrollView with Markdown support).
  - **Input Area:** `InputPanel` (Multiline text input + Action bar).
  - **Navigation:** `ModeTabBar` (Bottom Nav: 🎨 UI, 💻 CODE, 🔍 BUG, 🖼️ IMG).

## 3. Interaction Design
- **Buttons:** Flat, neon borders, subtle glow effect on hover/press.
- **Animations:** Minimalist, fast, "machine-like" (linear/ease-out).
- **Feedback:** Toast messages for successful actions (Copy/Save), clear Progress Indicator for AI operations.
