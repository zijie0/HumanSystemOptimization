---
name: human-system-optimization
description: Use when answering questions, teaching concepts, or drafting habit plans from the HumanSystemOptimization daily health practice knowledge base.
---

# Human System Optimization

Use this skill to help an agent answer questions and draft conservative life plans from this repository's health habit tutorial.

## Source Of Truth

Read these local artifacts before answering:

1. `references/index.json` for machine-readable modules, practices, cautions, references, and graph data.
2. `references/modules/*.md` for chapter-level explanations.
3. `README.md` when the user asks for original wording or full context.
4. `imgs/*.png` when answering about long-term diet, workout plans, longevity drugs, or cell reprogramming visuals.

Optional MCP access:

```bash
cd hso && uv run hso-mcp
```

The MCP server exposes:

- `list_modules`
- `search_knowledge`
- `get_module`
- `build_life_plan`
- `get_graph`

## Answering Rules

- Start from low-risk fundamentals: sleep, morning light, night light reduction, movement, reduced sugar, stable eating window, and focused work blocks.
- Preserve cautions. If a module has `cautions`, include relevant ones when giving advice.
- Do not present drugs, supplements, long fasting, or anti-aging interventions as routine recommendations.
- State that the knowledge base is for learning and habit design, not medical diagnosis or treatment.
- For medical conditions, abnormal lab values, pregnancy, minors, eating disorders, psychiatric concerns, chronic disease, or medication use, advise consultation with a qualified clinician.

## Planning Workflow

When drafting a plan:

1. Identify the user's focus: `sleep`, `diet`, `mindset_dopamine`, `learning_focus`, `brain_health`, `longevity`, `personal_practice`, or `general`.
2. Retrieve the module with MCP `get_module` or from `references/index.json`.
3. Select at most 3 actions for the first week.
4. Add tracking metrics from `tracking_metrics`.
5. Add a weekly review checkpoint.
6. Include relevant cautions and medical boundary text.

## Teaching Workflow

When helping the user absorb the material:

1. Explain the mechanism in plain language.
2. Give one concrete daily action.
3. Explain why the action maps to the mechanism.
4. Name one common failure mode.
5. Offer a short review question or self-check.

## Module Map

- `sleep`: sleep, circadian rhythm, morning light, night light, caffeine, NSDR.
- `diet`: intermittent fasting, eating windows, blood glucose, gut microbiome, fermented foods.
- `mindset_dopamine`: motivation, reward, dopamine baseline, addiction, growth mindset.
- `learning_focus`: neuroplasticity, errors, physiological sigh, attention, screen time.
- `brain_health`: aerobic exercise, Omega-3 EPA, choline, creatine, electrolytes.
- `longevity`: diet, exercise, monitoring, anti-aging drug controversy, cell reprogramming.
- `personal_practice`: author's practical routine and tool-based habit training.

## Safety Boundary

Use this exact boundary when the user asks for medical or high-risk advice:

> This repository supports health habit learning and planning. It is not a medical diagnosis, prescription, or treatment plan. For medications, supplements, prolonged fasting, chronic illness, abnormal lab values, pregnancy, minors, psychiatric concerns, or eating disorders, involve a qualified clinician.
