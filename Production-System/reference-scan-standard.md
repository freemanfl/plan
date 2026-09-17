# Reference Scan Standard

This is the required storage and analysis format for every reference website.

[Русская версия](reference-scan-standard.ru.md)

## Canonical package

```text
References/<category>/<site-slug>/
├── screenshots/
│   ├── desktop-full.png
│   ├── tablet-full.png
│   └── mobile-full.png
├── analysis.yaml
└── report.md
```

`analysis.yaml` is the canonical machine-readable record. `report.md` is the human-readable explanation and includes compact ASCII sketches for fast visual comparison. Screenshots are evidence. Do not put independent facts in the report that are absent from the YAML.

## Capture contract

Capture the same public page at three viewport sizes:

| File | Viewport |
| --- | --- |
| `desktop-full.png` | 1440 × 900 |
| `tablet-full.png` | 1024 × 768 |
| `mobile-full.png` | 390 × 844 |

Use full-page screenshots. Record the final URL, capture date, page state, cookie/banner handling, and any content that could not be captured. Dynamic or personalized pages must be treated as observations from one recorded state, not permanent facts.

## Required scan stages

Record these keys under `scan_status` in `analysis.yaml`:

```yaml
scan_status:
  screenshots: complete
  structure: complete
  content_mapping: pending
  visual_system: pending
  motion: pending
  implementation: pending
  final_report: pending
```

Allowed values are `pending`, `in_progress`, `complete`, and `not_applicable`.

## Analysis stages

### 1. Identity and context

Record site name, URL, category, page type, apparent audience, apparent business goal, primary conversion, capture metadata, and confidence notes.

### 2. Global shell

Record announcement bars, header type, logo position, navigation items, header actions, sticky behavior, footer structure, and persistent widgets.

### 3. Section inventory

List every visible section in order. Give each a stable ID, semantic role, approximate height, background treatment, entry/exit boundary, and evidence location.

### 4. Content mapping

For each section, map the actual content fields: eyebrow, heading, body, labels, calls to action, media, proof, metadata, form fields, and legal copy. Mark missing, inferred, or dynamic values.

### 5. Layout geometry

Describe container width, columns, alignment, whitespace, overlap, media ratio, card arrangement, density, and relationships between elements. Store numeric estimates where useful and confidence for inferred measurements.

### 6. Responsive transformation

Describe how each section changes across desktop, tablet, and mobile: stacking order, hidden elements, navigation changes, alignment, resizing, cropping, overflow, and spacing changes. Do not describe mobile as merely “stacked” when the order or function changes.

### 7. Visual system

Record typography roles, color roles, border and radius language, shadows, icon style, image treatment, repeated motifs, and design tokens that can be estimated reliably.

### 8. Interaction and motion

Record hover, focus, reveal, carousel, accordion, video, sticky, parallax, and transition behavior. A static screenshot cannot prove motion; verify interactively or mark it unverified.

### 9. Implementation interpretation

Separate four things:

- observation — directly visible or measured;
- inference — likely but not confirmed;
- recommendation — how the idea could be adapted;
- reusable pattern candidate — a finding worth comparing with other sites.

Document required assets, content prerequisites, accessibility risks, implementation complexity, performance risks, and a simpler substitute when the original effect is excessive.

## Report requirements

`report.md` must contain:

1. a short page summary;
2. desktop, tablet, and mobile ASCII sketches;
3. the ordered section table;
4. the conversion path;
5. key responsive transformations;
6. the smallest high-impact visual techniques;
7. content and asset prerequisites;
8. risks, unknowns, and confidence;
9. adaptation guidance without copying brand-specific expression.

## Minimum QA

- All three screenshots exist and open.
- The URL and capture date are recorded.
- Every visible section appears in the ordered inventory.
- Every section has content, layout, and responsive fields.
- Observations and recommendations are distinguishable.
- The report sketches agree with the section order.
- Status fields reflect actual completion.
- No claim based only on a screenshot is presented as verified interaction behavior.

