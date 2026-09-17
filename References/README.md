# Reference Websites

This directory stores website evidence by market category. The category helps discovery; the contents of every analyzed site follow one format.

[Русская версия](README.ru.md)

## Categories

- `normal/` — clear, conventional service or product funnels.
- `restaurant/` — restaurant and hospitality sites.
- `visual/` — image-led sites where conventional funnel layouts are intentionally broken.
- `tutor-education/` — tutoring, courses, and education businesses.
- `dance-studio-gym/` — dance, fitness, studio, and class-based businesses.

The complete candidate list and scan status live in [index.yaml](index.yaml).

## One format per analyzed site

```text
<category>/<site-slug>/
├── screenshots/
│   ├── desktop-full.png
│   ├── tablet-full.png
│   └── mobile-full.png
├── analysis.yaml
└── report.md
```

Follow the [reference scan standard](../Production-System/reference-scan-standard.md). `analysis.yaml` is the source of truth; `report.md` is the readable interpretation and contains the at-a-glance sketches.

Older section-first captures and superseded lists are in `Archive/`. They remain evidence, but they do not define the current workflow.

