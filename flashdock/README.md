# FlashDock Workstation Skills Pack (`flashdock/`)

This directory houses the specialized architectural, safety, and device-interaction skills created and used for developing **FlashDock** — the cross-platform Android flashing, unbricking, and emergency service workstation.

---

## Included Skills

| Skill | Focus | Key Highlights |
| :--- | :--- | :--- |
| **[`flashdock-workstation`](./flashdock-workstation/SKILL.md)** | FlashDock Architectural Standard | Zero-brick safety protocols, pre-flight partition verification, mandatory radio calibration backups (`efs`, `nvram`, `persist`), AVB/ARP anti-rollback guards, `QThread` async worker separation, vector SVG icons, macOS Big Sur design tokens, and automated version bumping. |
| **[`android-cli`](./android-cli/SKILL.md)** | Android CLI Tooling & Virtual Devices | Deep integration with `android`, `adb`, `fastboot`, Android SDK components, emulator management, UI inspection, logcat streaming, and official documentation lookups. |

---

## Safety & Architectural Principles

1. **Zero-Brick Guarantees**:
   - Verification of active slot (`_a` / `_b`), device battery $\ge 30\%$, and pre-flash calibration block backups before flashing.
2. **Asynchronous Architecture (`QThread`)**:
   - Zero blocking operations on the PySide6 UI thread. Clean worker lifecycle and cooperative cancellation.
3. **Multi-Chipset Hardware Detection**:
   - VID/PID priority mapping for MediaTek BROM/Preloader, Qualcomm EDL 9008, Unisoc FDL, Fastboot, and ADB.
4. **Vector UI Standards**:
   - 100% SVG vector assets rendered via dynamic icon generators, preventing native C++ teardown violations on modern Python runtimes.

---

## Installation & Enabling in Your Agent

### 1. Workspace-Level (Recommended for FlashDock Projects)
```powershell
$workspace = "C:\Path\To\FlashDock"
New-Item -ItemType Directory -Force -Path "$workspace\.agents\skills"
Copy-Item -Recurse -Force "flashdock\*" "$workspace\.agents\skills\"
```

### 2. Global Installation
```powershell
$globalSkills = "$env:USERPROFILE\.gemini\config\skills"
New-Item -ItemType Directory -Force -Path $globalSkills
Copy-Item -Recurse -Force "flashdock\*" "$globalSkills\"
```
