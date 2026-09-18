# Web Studio Design System & Effects Library

## Purpose

This document stores the visual rules and reusable design intelligence that sit **above layout geometry**.

- **Layout Library** = where elements go.
- **Design System** = how selected layouts look and work together.
- **Effects Library** = optional motion, interaction, and visual enrichment applied after the base design is sound.

The goal is to reduce visual quality from subjective improvisation into reusable rules, references, and components that AI can apply predictably.

---

## 1. Base Design System

### 1.1 Typography
Store reusable rules for:
- hero H1 scale;
- section heading scale;
- body size and line-height;
- eyebrow/category text;
- card title scale;
- readable line lengths;
- font pairing rules;
- mobile scaling.

Useful starting principle from strong small-business references:
- limited number of sizes;
- strong hierarchy;
- restricted text widths;
- avoid long full-width paragraphs.

### 1.2 Spacing
Store:
- section padding ranges;
- internal component spacing;
- gaps between cards;
- spacing rhythm between eyebrow, heading, body, proof, and CTA;
- mobile reductions.

Professional appearance often comes from **generous and consistent spacing**, not complex components.

### 1.3 Surfaces and Components
Store rules for:
- border radius families;
- button shapes;
- card padding;
- borders/shadows;
- background alternation;
- image framing;
- icon treatment;
- button hierarchy;
- surface contrast.

### 1.4 Imagery
Store:
- preferred aspect ratios by section type;
- when to use full bleed vs framed images;
- crops and focal-point rules;
- whether images act as decoration, proof, or the main selling asset;
- minimum image quality needed for visual-dominant layouts.

---

## 2. Whole-Page Composition Rules

These rules govern how layouts work together across a page.

- Avoid repeating the same section shape several times in a row.
- Avoid multiple visually heavy sections back-to-back unless intentional.
- Alternate text-heavy and media-heavy compositions where useful.
- Keep spacing transitions deliberate.
- Maintain color and surface continuity.
- Balance visual weight across the page.
- Keep animation intensity controlled.
- Use repetition for consistency, but controlled variation to avoid template fatigue.

---

## 3. Theme

A **theme** is a loose semantic motif derived from the business, subject, place, history, culture, product, or personality.

It is not a rigid template. It is a creative constraint used to find a small number of context-specific design opportunities.

Examples:
- history / archaeology → archival treatments, timeline transitions, subtle artifact motifs;
- football → pitch geometry, path motion, scoreboard-inspired details;
- dance → movement, flowing transitions, choreography-inspired gallery behavior;
- hospitality → atmosphere, locality, materials, texture, place-based imagery.

Rule:

**Theme should enrich the site, not turn it into a gimmick.**

Useful AI instruction pattern:

> Theme: [subject]. Find 2–4 subtle opportunities where the theme can influence interaction, decoration, imagery treatment, or motion without reducing usability.

---

## 4. Effects / Design Intelligence Library

Build a curated library of effects found on strong real websites instead of expecting AI to invent visual sophistication every time.

Each effect should ideally store:
- ID / name;
- category;
- source/reference;
- screenshot/video if available;
- plain-English description;
- trigger: load / viewport / scroll / hover / cursor / click;
- target element;
- initial state;
- final state;
- timing / easing / stagger;
- why it works;
- suitable section types;
- suitable business types;
- media/content requirements;
- intensity: subtle / noticeable / centerpiece;
- mobile fallback;
- accessibility/performance notes;
- implementation/component reference;
- concise AI instructions.

### Initial effect primitives

#### viewport_reveal_01
- trigger: element enters viewport;
- initial: opacity 0, translateY roughly 20–35px;
- final: opacity 1, translateY 0;
- duration: roughly 450–700ms;
- optional child stagger: 60–120ms;
- use for headings/cards selectively, not every element.

#### card_hover_01
- trigger: pointer hover;
- card lift: roughly -4px;
- image scale: roughly 1.02–1.04;
- duration: roughly 200–350ms;
- use for service/portfolio cards where hover feedback improves perceived polish.

#### image_mask_reveal_01
- trigger: viewport/scroll;
- image begins partially clipped or masked;
- mask expands/reveals the image;
- pair with subtle text fade/raise;
- best used sparingly as a polished section entrance.

---

## 5. Reference Design Grammar

### IHI / Build 76-type professional service sites
A polished result can come from a small number of repeatable levers:
- generous section spacing;
- strong but limited typography ratios;
- restricted readable content widths;
- a small number of dominant visual masses per section;
- consistent radii, buttons, spacing, and card padding;
- repetition with controlled variation;
- subtle motion rather than constant animation.

This is important because it shows that perceived quality does not require exotic WebGL or bespoke engineering.

---

## 6. Processing Order

**Purpose → Funnel → Content → Layout → Base Design → Theme → Effects / Enrichment → Final Polish / QA**

Do not let AI jump directly from content to animation or decorative styling.
