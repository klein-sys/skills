# Design Token Architecture Guide

A professional design system organizes tokens into three tiers: Global Tokens, Semantic Tokens, and Component Tokens.

---

## The Three-Tier Token Model

```
[Tier 1: Global Primitives]
 (Raw colors, font names, scale factors: --blue-600: #2563eb, --font-sans: 'Inter')
               │
               ▼
[Tier 2: Semantic Tokens]
 (Meaningful context mappings: --color-primary, --surface-card, --text-secondary)
               │
               ▼
[Tier 3: Component Tokens]
 (Scoped component overrides: --btn-bg, --card-border, --nav-height)
```

### Why Three Tiers?
- If the brand color changes from Royal Blue to Violet, only Tier 2 (`--color-primary`) changes.
- Dark mode simply rebinds Semantic Tokens (`--surface-bg: var(--gray-900)`) without touching component classes.

---

## Token Organization Blueprint

```css
:root {
  /* 1. Global Primitives */
  --slate-950: #020617;
  --slate-900: #0f172a;
  --slate-800: #1e293b;
  --slate-700: #334155;
  --slate-100: #f1f5f9;
  --slate-50:  #f8fafc;

  --indigo-500: #6366f1;
  --indigo-600: #4f46e5;
  --indigo-700: #4338ca;
  --emerald-500: #10b981;
  --rose-500: #f43f5e;

  /* 2. Semantic Tokens - Light Theme Default */
  --bg-app: var(--slate-50);
  --bg-surface: #ffffff;
  --border-subtle: rgba(15, 23, 42, 0.08);
  --text-main: var(--slate-900);
  --text-muted: var(--slate-700);
  --color-primary: var(--indigo-600);
  --color-primary-hover: var(--indigo-700);
  --color-success: var(--emerald-500);
  --color-danger: var(--rose-500);

  /* 3. Spacing Baseline */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;

  /* 4. Elevation Shadows */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -2px rgba(0, 0, 0, 0.04);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
  --shadow-glow: 0 0 20px -3px rgba(99, 102, 241, 0.35);

  /* 5. Radii */
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-full: 9999px;
}

[data-theme="dark"] {
  --bg-app: var(--slate-950);
  --bg-surface: var(--slate-900);
  --border-subtle: rgba(255, 255, 255, 0.08);
  --text-main: var(--slate-50);
  --text-muted: #94a3b8;
  --color-primary: var(--indigo-500);
  --color-primary-hover: var(--indigo-600);
}
```
