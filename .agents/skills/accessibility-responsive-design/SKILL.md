---
name: accessibility-responsive-design
description: >-
  Use this skill when implementing responsive layouts across mobile, tablet, and desktop viewports, or when
  auditing and optimizing web accessibility for WCAG 2.1 AA compliance. Enforces mobile-first responsive design,
  fluid typography, keyboard navigability, semantic HTML, and ARIA patterns.
---

# Accessibility & Responsive Design

This skill ensures your web applications are inclusive, accessible, and seamlessly responsive across all devices and screen sizes. It enforces **WCAG 2.1 Level AA** compliance, semantic HTML, accessible keyboard navigation, and modern fluid layouts.

---

## When to Activate This Skill

- When designing or refactoring responsive layouts across mobile (<640px), tablet (640px-1024px), and desktop (>1024px).
- When implementing interactive UI components that require keyboard navigation (dialogs, dropdowns, menus, tabs).
- When auditing visual contrast, focus indicators, or screen-reader usability.
- When supporting user accessibility preferences (`prefers-reduced-motion`, high contrast, dark mode).

---

## Core Implementation Workflow

```
[Mobile-First Viewport Strategy]
               │
               ▼
[Semantic HTML & Landmark Hierarchy]
               │
               ▼
[WCAG 2.1 AA Contrast & Color Verification]
               │
               ▼
[Keyboard Traversal & Focus Management]
               │
               ▼
[Screen-Reader ARIA & Live Regions]
               │
               ▼
[Reduced Motion & Accessibility Media Queries]
```

### 1. Mobile-First & Fluid Layout Foundations
- **Base Style on Smallest Screens**: Write default styles for 320px–375px viewports first; use `min-width` media queries for larger viewports:
  ```css
  /* Mobile default */
  .grid-container { display: flex; flex-direction: column; gap: 16px; }
  
  /* Desktop enhancement */
  @media (min-width: 768px) {
    .grid-container { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
  }
  ```
- **Fluid Typography**: Use `clamp()` to scale typography smoothly without jumpy breakpoints:
  ```css
  font-size: clamp(1.125rem, 1rem + 0.5vw, 1.5rem);
  ```
- **Touch Target Sizes**: All interactive elements (buttons, links, inputs) must be at least `44x44px` on mobile.
See [Responsive Layout Grid Guide](./references/responsive-layout-grid.md).

### 2. WCAG 2.1 Level AA Compliance
1. **Color Contrast Ratios**:
   - Normal text (< 18pt or < 14pt bold): Minimum **4.5:1** contrast against background.
   - Large text (≥ 18pt or ≥ 14pt bold): Minimum **3.0:1** contrast.
   - UI components and graphical objects: Minimum **3.0:1** contrast against adjacent colors.
   - Never convey information using color alone (pair colored indicators with text or icons).
2. **Visible Focus Rings**:
   - Never suppress `outline: none` without providing an explicit `:focus-visible` replacement.
   - Focus indicator must have at least **3:1** contrast against the background.

### 3. Keyboard Navigation & Focus Trapping
- **Full Keyboard Accessibility**: All interactive elements must be reachable via `Tab` and activatable via `Enter` / `Space`.
- **Modal Dialogs Focus Trap**:
  - When a modal opens, trap keyboard focus within the dialog.
  - Pressing `Escape` must dismiss the modal and restore focus to the triggering element.
- **Logical Tab Order**: Match visual reading order (left-to-right, top-to-bottom). Do not use positive `tabindex` values (`tabindex="1"` is forbidden).

### 4. Semantic HTML & ARIA Patterns
- **Rule of ARIA**: Use native HTML5 elements (`<button>`, `<dialog>`, `<nav>`, `<input>`) before reaching for ARIA attributes.
- **Mandatory Landmarks**: Every page must have one `<main>` landmark, clear `<header>` / `<nav>`, and `<footer`>.
- **Dynamic Content**: Use `aria-live="polite"` for non-critical status updates, `aria-live="assertive"` for urgent error messages.
See [WCAG 2.1 AA Checklist](./references/wcag-21-aa-checklist.md) and [Accessible Component Patterns](./examples/accessible-component-patterns.md).

### 5. Accessibility Media Queries
Respect user system preferences:
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

---

## References & Guides

- [WCAG 2.1 Level AA Comprehensive Checklist](./references/wcag-21-aa-checklist.md)
- [Responsive Layout & Fluid Grid Guide](./references/responsive-layout-grid.md)
- [Accessible Component Patterns (Modals, Dropdowns, Forms)](./examples/accessible-component-patterns.md)

---

## Verification Checklist

Before approving any UI implementation:

- [ ] Page passes automated contrast checks (4.5:1 minimum for normal text).
- [ ] Interface is 100% operable via keyboard alone with clearly visible focus rings.
- [ ] Layout renders cleanly without horizontal scrolling from 320px up to 2560px.
- [ ] Touch targets on mobile meet or exceed 44x44 CSS pixels.
- [ ] `prefers-reduced-motion` is implemented to disable intense animations.
- [ ] Forms have explicit `<label>` bindings and `aria-describedby` error associations.
