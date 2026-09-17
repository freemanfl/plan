# Production System

This directory defines one operational path from raw client information to a finished, maintainable website. It is the source of truth for production work.

[Русская версия](README.ru.md)

## Pipeline

1. Collect customer facts and assets.
2. Resolve missing or contradictory inputs.
3. Define the primary audience, business goal, conversion action, and constraints.
4. Build the page architecture and content hierarchy.
5. Select relevant reference evidence by problem, not by appearance alone.
6. Define each section's content, layout, behavior, and responsive transformation.
7. Apply the visual system and restrained finishing effects.
8. Implement the page.
9. Test content completeness, responsiveness, accessibility, performance, SEO, forms, and analytics.
10. Record reusable findings.
11. Hand off and maintain the result.

## Canonical contracts

| Contract | Purpose |
| --- | --- |
| [Customer data schema](customer-data-schema.md) | Minimum facts, copy, assets, proof, logistics, and constraints needed to generate a competent site. |
| [Visual structure schema](visual-structure-schema.md) | Machine-readable page, section, layout, responsive, and visual decisions. |
| [Reference scan standard](reference-scan-standard.md) | How a reference website is captured, analyzed, and stored. |
| [Layout library](layout-library.md) | Candidate layout families and selection logic. |
| [Design system and effects](design-system-effects.md) | Tokens, components, and low-complexity finishing techniques. |
| [Technical QA](technical-qa.md) | Release and maintenance checks. |

## Decision order

Decide in this order: business goal → required content → information priority → layout → visual styling → effects. A striking reference never overrides the client's actual content, budget, or conversion needs.

The default quality target is polished and credible, not maximalist luxury. Prefer the smallest visual intervention that produces a meaningful improvement. Avoid effects that are large, fragile, slow, or difficult to maintain.

## Reference role

References are evidence, not templates to copy. A scan records what exists, how it works, what inputs it requires, and where it may be useful. Reusable conclusions move to `Pattern-Library/` only after validation.

Every reference uses the canonical folder described in the [reference scan standard](reference-scan-standard.md).

## Status discipline

A captured screenshot is not a completed analysis. Track stages explicitly. Use `pending`, `in_progress`, `complete`, or `not_applicable`; never infer completion from the presence of a file.

