# Web Studio System

This repository is the operating system for the studio: business decisions, customer inputs, reference analysis, design rules, implementation guidance, and quality assurance.

Discussion can happen in chat. Decisions, specifications, and reusable knowledge belong here.

[Русская версия](README.ru.md)

## One production pipeline

Customer data → business goal and conversion → page architecture → content hierarchy → reference-informed layout → visual system → implementation → QA → maintenance.

Every document in this repository supports that sequence. When two documents overlap, the file named as the source of truth in [Production System](Production-System/README.md) wins.

## Start here

- [Business master plan](Business/master-plan.md)
- [Production system](Production-System/README.md)
- [Customer data schema](Production-System/customer-data-schema.md)
- [Reference scan standard](Production-System/reference-scan-standard.md)
- [Technical QA](Production-System/technical-qa.md)

## Repository map

- `Business/` — offer, sales, legal, operations, and strategy.
- `Production-System/` — the canonical website-generation process and its contracts.
- `References/` — one standardized evidence package per reference website.
- `Pattern-Library/` — reusable patterns promoted only after they have been validated.
- `Sandbox/` — experiments and temporary work; never a source of truth.
- `Archive/` — superseded material retained for provenance.

## Working rules

1. Update the canonical document instead of creating another explanation of the same idea.
2. Put every scanned website in the standard reference format.
3. Keep observations separate from recommendations and reusable patterns.
4. Promote a pattern only after comparison across multiple references or production use.
5. Archive replaced material; do not silently keep two active versions.
6. English filenames and schema keys are canonical. Russian files explain the same system and use the `.ru.md` suffix.

