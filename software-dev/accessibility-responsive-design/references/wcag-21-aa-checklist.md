# WCAG 2.1 Level AA Compliance Checklist

## Principle 1: Perceivable

- [ ] **1.1.1 Non-text Content**: All images, icons, and non-text visual content provide meaningful `alt` text or `aria-hidden="true"` if purely decorative.
- [ ] **1.3.1 Info and Relationships**: Information, structure, and relationships are determined programmatically (proper heading hierarchy `h1` -> `h2` -> `h3`, table headers `<th>`, list markup `<ul>`/`<ol>`).
- [ ] **1.4.1 Use of Color**: Color is never the sole visual means of conveying information, indicating an action, or prompting a response.
- [ ] **1.4.3 Contrast (Minimum)**: Text and images of text have a contrast ratio of at least **4.5:1** (or **3:1** for text ≥ 18pt / 14pt bold).
- [ ] **1.4.4 Resize Text**: Text can be zoomed up to 200% without loss of content or functionality.
- [ ] **1.4.10 Reflow**: Content reflows without loss of information and without requiring scrolling in two dimensions on a 320px screen.

---

## Principle 2: Operable

- [ ] **2.1.1 Keyboard**: All functionality is available using only a keyboard.
- [ ] **2.1.2 No Keyboard Trap**: Keyboard focus never gets permanently trapped in any sub-component.
- [ ] **2.4.1 Bypass Blocks**: A "Skip to Main Content" mechanism is provided at the very top of the page.
- [ ] **2.4.3 Focus Order**: Navigation sequence through components is logical and preserves meaning.
- [ ] **2.4.7 Focus Visible**: The keyboard focus indicator is always distinctly visible.
- [ ] **2.5.5 Target Size**: Pointer inputs / touch targets are at least **44 by 44 CSS pixels**.

---

## Principle 3: Understandable

- [ ] **3.1.1 Language of Page**: The default human language is declared via `<html lang="en">`.
- [ ] **3.2.1 On Focus**: When any component receives focus, it does not unexpectedly initiate a context change (like submitting a form or opening a popup).
- [ ] **3.3.1 Error Identification**: If an input error is detected, the item in error is identified and described in text.
- [ ] **3.3.2 Labels or Instructions**: Form fields provide explicit labels or instructions.

---

## Principle 4: Robust

- [ ] **4.1.2 Name, Role, Value**: For all UI components, the name and role can be programmatically determined by assistive technologies (using semantic HTML or correct ARIA roles).
