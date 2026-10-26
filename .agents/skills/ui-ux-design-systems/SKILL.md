---
name: ui-ux-design-systems
description: >-
  Use this skill when designing web interfaces, creating frontend component design systems, selecting
  color palettes and typography, or refining UI aesthetics. Banishes generic AI-generated templates in favor
  of intentional design tokens, harmonious palettes, bento layouts, and polished micro-interactions.
---

# UI/UX Design & Design Systems

This skill acts as a senior UI/UX designer and design technologist. It guides you in building distinctive, intentional, and high-fidelity user interfaces powered by structured design tokens, curated typography, and bespoke visual themes.

---

## When to Activate This Skill

- When designing or building a web application, dashboard, landing page, or component library.
- When establishing or refactoring CSS design tokens (colors, typography, spacing, shadows, radii).
- When upgrading a plain or generic UI into a premium, state-of-the-art visual experience.
- When designing complex UI components (bento grids, cards, modals, navigation, data tables).

---

## UI/UX Design Workflow

```
[Define Brand Persona & Aesthetic Theme]
                  │
                  ▼
   [Establish Design Token Hierarchy]
    - Neutral & Semantic Color Scales
    - Typography Scale & Font Pairing
    - Spacing (4px/8px) & Elevation
                  │
                  ▼
 [Assemble Component Primitives & States]
    - Default, Hover, Active, Focus, Disabled
                  │
                  ▼
[Apply Layout Hierarchy & Bento Composition]
                  │
                  ▼
[Polish Micro-Interactions & Transitions]
```

### 1. Select a Distinct Aesthetic Theme
Never settle for default, generic templates. Select a deliberate aesthetic matching the application's domain:
- **Dark Modern Cyber / High-Tech**: Deep slate/charcoal backgrounds (`#0B0F17`), subtle 1px border glows (`rgba(255,255,255,0.08)`), vibrant electric accents (cyan, violet, emerald).
- **Refined SaaS Minimalist**: Warm crisp whites (`#FAFAFA`), subtle neutrals, high-contrast dark typography (`#111827`), elegant neutral shadows, royal blue or indigo primary.
- **Glassmorphism / Frosted Modern**: Multi-layer translucent backdrops (`backdrop-filter: blur(16px)`), subtle specular borders (`rgba(255, 255, 255, 0.12)`), soft gradient background meshes.
- **Modern Bento Grid**: Asymmetric modular cards, rounded corners (`16px` to `24px`), content-dense sections with visual hierarchy.
See [Anti-Generic Design Rules](./references/anti-generic-design-rules.md).

### 2. Design Token Architecture (CSS Custom Properties)
All visual properties must be derived from structured CSS tokens:
- **Colors**: Never use raw hex codes directly in component classes. Map `--color-primary`, `--color-surface`, `--color-text-main`, `--color-text-muted`.
- **Typography Scale**: Define paired fonts from Google Fonts (e.g., `Outfit` or `Plus Jakarta Sans` for headings, `Inter` or `Geist` for body).
- **Spacing Scale**: 4px/8px baseline (`--space-1: 4px`, `--space-2: 8px`, `--space-4: 16px`, `--space-6: 24px`, `--space-8: 32px`).
- **Radius & Shadows**: `--radius-sm: 6px`, `--radius-md: 10px`, `--radius-lg: 16px`, `--shadow-card`.
See [Design Token Architecture](./references/design-token-architecture.md) and [Curated Palettes & Typography](./references/curated-palettes-typography.md).

### 3. Component States & Micro-Interactions
Every interactive element must have distinct, deliberate states:
- **Resting**: Balanced contrast, readable typography.
- **Hover**: Subtle lift (`transform: translateY(-2px)`), enhanced shadow, brightness bump (`1.05`).
- **Focus**: Distinct, accessible focus ring (`outline: 2px solid var(--color-accent); outline-offset: 2px`).
- **Active / Pressed**: Subtle scale down (`transform: scale(0.98)`).
- **Disabled**: Lower opacity (`0.5`), cursor not-allowed, stripped click events.

---

## References & Guides

- [Design Token Architecture Guide](./references/design-token-architecture.md)
- [Curated Palettes & Typography Pairings](./references/curated-palettes-typography.md)
- [Anti-Generic Design Rules](./references/anti-generic-design-rules.md)
- [Production Ready CSS Design System Example](./examples/component-tokens-css-example.css)

---

## Verification Checklist

Before finalizing any frontend interface:

- [ ] All colors, fonts, spacing, and shadows use CSS variables/tokens rather than ad-hoc inline values.
- [ ] Typography uses modern, curated fonts with clear scale hierarchy and line heights.
- [ ] Every button, link, and input has designed hover, focus-visible, and active states.
- [ ] Visual design avoids generic "AI-generated" tropes (no purple-on-black cards without brand justification).
- [ ] High contrast ratios are maintained between text and background surfaces.
