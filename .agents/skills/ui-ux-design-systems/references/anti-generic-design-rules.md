# Anti-Generic Design Rules: Banishing AI Template Aesthetics

AI-generated web pages often suffer from stereotypical design patterns that signal low quality and lack of intention. Use these rules to craft interfaces that look hand-crafted and bespoke.

---

## 1. The Prohibited "AI Template" Tropes

| Prohibited Pattern | Why It Fails | What To Do Instead |
| :--- | :--- | :--- |
| **Cliché Purple/Magenta Gradient on Black** | Overused in 90% of AI demos; feels lazy and generic. | Pick a domain-grounded palette (e.g., Deep Emerald + Slate, Warm Ochre + Charcoal). |
| **Random Colored Pill Badges** | Putting "01", "02", "03" or "NEW" everywhere with bright backgrounds creates visual noise. | Use numbering only if it represents an actual ordered workflow or timeline. |
| **Unstyled Default Browser Focus Outline** | Ugly blue fuzzy outline breaks custom aesthetics. | Craft custom `:focus-visible` rings matching brand accent tokens with `outline-offset: 2px`. |
| **Uniform 3-Column Card Grids** | Makes every landing page look like an identical Bootstrap theme. | Use an asymmetric **Bento Grid** with varying card spans (e.g., 2-col hero card + 1-col metric card). |
| **Centered Wall of Centered Text** | Centered paragraphs longer than 2 lines are difficult to read. | Left-align body paragraphs; reserve center alignment strictly for short hero titles. |

---

## 2. Hallmarks of Intentional, Premium Design

1. **Subtle Surface Depth**:
   Instead of flat borders or harsh drop shadows, use multi-layer depth:
   - A 1px translucent border (`rgba(255, 255, 255, 0.08)`).
   - An ambient diffused shadow (`0 20px 25px -5px rgba(0, 0, 0, 0.2)`).
   - A subtle top inset highlight (`box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1)`).
2. **Typography Hierarchy**:
   - Limit to 2 font families maximum.
   - Establish high contrast between headings (bold, tight letter-spacing: `-0.02em`) and body (regular weight, line-height: `1.6`).
3. **Micro-Interactions**:
   - Provide tactile visual feedback on hover (`translateY(-2px)`, subtle glow, or border brightness shift).
   - Smooth transition timing (`transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1)`).
