# Responsive Layout & Fluid Grid Guide

## 1. Breakpoint Conventions

Use content-driven breakpoints aligned with modern device categories:

| Breakpoint Name | Media Query | Target Devices | Typical Layout Strategy |
| :--- | :--- | :--- | :--- |
| **`sm` (Mobile)** | `< 640px` | Phones (Portrait) | Single column, full-width inputs, collapsible drawer navigation. |
| **`md` (Tablet)** | `≥ 768px` | Tablets, Large Phones | 2-column grid, compact sidebar, visible top bar actions. |
| **`lg` (Laptop)** | `≥ 1024px` | Laptops, Desktops | 3 or 4-column bento grids, persistent navigation sidebar. |
| **`xl` (Wide)** | `≥ 1280px` | Large Monitors | Max-width content container (`max-width: 1280px; margin: 0 auto`). |

---

## 2. Modern Fluid CSS Grid Without Media Queries

Instead of brittle breakpoint overrides, use CSS Grid `auto-fit` with `minmax()`:

```css
.auto-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr));
  gap: var(--space-6, 24px);
}
```

### Why this excels:
- Automatically adapts from 1 column on a 320px phone to 4 columns on an ultrawide monitor without a single media query.
- `min(100%, 280px)` prevents overflow on viewports smaller than 280px.

---

## 3. Container Queries (`@container`)

When a component appears in both a wide hero section and a narrow sidebar, style it based on its container's width rather than the screen viewport:

```css
.card-wrapper {
  container-type: inline-size;
}

@container (min-width: 450px) {
  .product-card {
    display: flex;
    flex-direction: row;
    align-items: center;
  }
}
```
