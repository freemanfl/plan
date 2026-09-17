# Web Studio Layout Library

## Purpose

This file stores reusable website section layouts as structured design blueprints.

It is intentionally separate from the Master Plan:

- **Master Plan** = explains the business, system, logic, and why.
- **Layout Library** = stores concrete reusable section geometries and layout references.

The goal is to turn visual composition from an open-ended design wildcard into a constrained system that AI can select, populate, and adapt predictably.

---

## Core Rule

A layout describes **structure and geometry**, not final visual style.

Layout answers:
- where elements go;
- how much space they occupy;
- their order and hierarchy;
- media requirements;
- CTA placement;
- responsive collapse behavior.

Design, theme, typography styling, colors, surfaces, and effects are applied later.

---

## Standard Layout Data Shape

Each layout should eventually store as much of the following as useful:

```yaml
id: unique_layout_id
section_type: hero | services | proof | testimonials | offer | cta | gallery | etc
family: optional loose category

frame:
  max_width:
  min_height:
  section_padding:

grid:
  columns:
  gap:

regions:
  - name:
    columns:
    vertical_anchor:
    relative_weight:

content_stack:
  - eyebrow
  - heading
  - body
  - proof
  - cta

content_constraints:
  heading_lines_max:
  body_length_target:
  cta_count:

media:
  count:
  aspect_ratio:
  role:

responsive:
  tablet:
  mobile:

usage:
  works_well_for:
  avoid_when:

reference:
  site:
  screenshot:
  notes:
```

The schema can evolve. It should remain practical rather than becoming bureaucracy.

---

# Hero Layouts

## Captured Reference Layouts

The earlier hero-section captures are retained in `Archive/legacy-reference-captures/`. They have not yet been converted to the current per-site reference format and therefore are evidence, not an active catalogue.

These are untested reusable abstractions, not exact source-code reconstructions or completed components. Proposed dimensions and mobile rules are distinguished from screenshot observations. The four current families are split, background overlay, text-first, and search-led. Existing blueprints below remain as earlier starting references.

## hero_service_split_01

### Reference
Oak Harbor / IHI-type professional service-business hero.

### Structure

```yaml
id: hero_service_split_01
section_type: hero
family: split

frame:
  max_width: 1200-1320px
  min_height: 75-90vh

grid:
  columns: 12
  gap: 24-40px

regions:
  - name: copy
    columns: 1-6
    vertical_anchor: center
    relative_weight: 0.45

  - name: visual
    columns: 7-12
    vertical_anchor: center
    relative_weight: 0.55

content_stack:
  - eyebrow
  - h1
  - supporting_copy
  - trust_or_benefit_row
  - primary_cta
  - secondary_cta

visual_stack:
  - dominant_visual
  - proof_or_stat_1
  - proof_or_stat_2
  - proof_or_stat_3

responsive:
  mobile:
    order: copy_then_visual
    columns: 1
    ctas: stacked_or_full_width
```

### Why it works
- Strong information hierarchy.
- Easy to understand immediately.
- Visual side can carry proof rather than functioning as decoration only.
- Highly reusable for local service businesses.

---

## hero_centered_offer_01

### Reference
ShipFast-type direct-response hero.

```yaml
id: hero_centered_offer_01
section_type: hero
family: centered

alignment: center

content_widths:
  headline: ~8/12 columns
  supporting_copy: ~6/12 columns

content_stack:
  - outcome_headline
  - mechanism_or_supporting_sentence
  - primary_cta
  - scarcity_or_proof_micro_row
  - large_product_or_proof_visual

media:
  width: 70-90% of content container
  position: below_copy

responsive:
  mobile:
    maintain_centered_axis: true
    media_width: near_full
```

### Best suited to
- Simple offers.
- Productized services.
- Strong single-value propositions.
- Cases where the main visual is proof/product UI.

---

## hero_visual_dominant_01

### Structure

```yaml
id: hero_visual_dominant_01
section_type: hero
family: full_bleed_visual

visual:
  dominant: true
  placement: background_or_large_frame

copy:
  width: narrow_to_medium
  overlay_or_adjacent: true

content_stack:
  - eyebrow_optional
  - h1
  - supporting_copy
  - cta
```

### Best suited to
- Photography.
- Hospitality.
- Restaurants.
- Architecture.
- Businesses with excellent visual material.

### Avoid when
- Client imagery is weak.
- The offer needs dense explanation above the fold.

---

## hero_text_first_01

### Structure

```yaml
id: hero_text_first_01
section_type: hero
family: text_first

visual_weight:
  copy: high
  media: low

content_stack:
  - eyebrow
  - large_h1
  - concise_body
  - cta_group
  - proof_row
```

### Best suited to
- Strong proposition.
- Consultants.
- Professional services.
- Sites where credibility and copy matter more than imagery.

---

# Service Layouts

## services_grid_3_equal_01

### Reference
IHI-type three-service grid.

```yaml
id: services_grid_3_equal_01
section_type: services

columns:
  desktop: 3
  tablet: 2
  mobile: 1

cards:
  equal_height: true
  image_ratio: 4/3
  title_lines_max: 2
  body_lines_target: 2-4
  cta_position: bottom
  internal_padding: generous

section_stack:
  - eyebrow_optional
  - section_heading
  - short_intro
  - card_grid
  - optional_view_all_cta
```

### Design intent
Professional appearance comes from consistency: equal media ratios, controlled copy length, shared spacing, and aligned CTAs.

---

## Services reference conversion — 2026-08-31

The earlier service-section captures are retained in `Archive/legacy-reference-captures/`. They have not yet been converted to the current per-site reference format and therefore are evidence, not an active catalogue.

The legacy entries cover five structural families: card grids, split lists, introduction splits, programme grids, and lists around a central visual. These are untested observations; no production implementation is implied. Validated, reusable findings belong in `Pattern-Library/`.

# Trust / Proof Layouts

## stats_band_4_01

### Reference
IHI-type oversized statistics band.

```yaml
id: stats_band_4_01
section_type: proof

columns:
  desktop: 4
  mobile: 2

hierarchy:
  number: 1.0
  label: 0.35
  explanation: 0.22

content_per_item:
  - dominant_number
  - short_label
  - optional_explanation
```

### Why it works
A very simple structure can create strong perceived legitimacy when the numbers dominate visually and the supporting text remains restrained.

---

# Testimonial Layouts

## testimonials_variable_01

### Problem handled
Testimonials often vary heavily in length. The layout should not blindly force every quote into identical cards.

```yaml
id: testimonials_variable_01
section_type: testimonials

items:
  minimum: 3
  preferred: 4-6

long_quote_strategy:
  - featured_card
  - carousel
  - clamp_with_expand

short_quote_strategy:
  - secondary_card
  - compact_grid_item

identity_required: true
```

---

# CTA Layouts

## closing_conversion_01

### Reference
IHI-type final conversion block.

### Logic
The closing CTA compresses the main promise after the page has already explained and proven it.

```yaml
id: closing_conversion_01
section_type: cta

content_stack:
  - repeated_primary_promise
  - short_supporting_copy
  - reassurance_bullets
  - primary_cta
  - secondary_cta_optional
  - contact_method_optional
```

---

# Reference Sites

## Fraser Water Services
https://www.fraserwaterservices.co.uk/

Useful as a **clean professional service-business baseline**.

Approximate page structure:

**Hero → trust/proof → service focus → service grid → testimonial → CTA → credentials/footer**

Why it matters:
- visually strong without complex architecture;
- highly reproducible;
- quality comes from spacing, typography, imagery, hierarchy, and consistency.

---

## IHI Ltd
https://www.ihiltd.co.uk/

Useful as a **polished but structurally ordinary small-business landing page**.

Approximate structure:

**Hero → Services → Trust/Statistics → Testimonials → Final Conversion Block → Footer**

Reusable primitives identified:
- split hero with proof embedded into visual side;
- three-card services grid;
- four-column oversized-stat band;
- testimonial layout that tolerates variable quote lengths;
- closing CTA that repeats the main promise in compressed form.

---

# Future Layout Library Work

Add layouts section by section rather than trying to create hundreds at once.

Likely categories:
- Hero
- Problem
- Benefits
- Services
- Process
- Proof / Stats
- Portfolio / Gallery
- Testimonials
- Pricing / Offer
- FAQ
- Booking
- Team / About
- Location / Contact
- CTA
- Footer

For strong real-world examples, capture:
1. screenshot/reference;
2. structural geometry;
3. content requirements;
4. responsive behavior;
5. why it works;
6. when to use it;
7. implementation/component reference later.

---

# Section Buckets — Core and Optional

Added 2026-08-31 following the Build 76 homepage review and discussion. This organizes reference collection by section purpose. It is not a compulsory page sequence or a claim that every bucket appears on most reviewed sites.

A bucket describes what a section does. Layout variants describe its arrangement; design and effects describe its appearance and behavior. Header and footer are included as reusable site-wide structures.

## Core Collection Buckets

| Bucket | Purpose |
|---|---|
| Header / Navigation | Identify the business and provide navigation and primary actions. |
| Hero | Introduce the proposition and the visitor's next step. |
| Services / Products / Programmes | Explain the available offering. |
| About / Benefits / Why Choose Us | Explain the business, its approach, and reasons to choose it. |
| Trust / Credentials / Statistics | Present factual evidence: qualifications, accreditations, client logos, and meaningful numbers. |
| Testimonials / Reviews | Present attributed customer feedback or verified ratings. |
| CTA / Contact | Prompt and enable an inquiry, quote, call, or other next step. |
| Footer | Provide supporting navigation, business details, contact routes, and legal links. |

Core means a priority for building the library, not mandatory on every site. A small trust row inside a hero is not a separate section. Omit unsupported proof rather than inventing statistics, logos, or testimonials.

## Secondary / Optional Collection Buckets

The examples identified in the reviewed sites include process, FAQ, featured offers, galleries/listings, team, news/promotions, coverage, and interactive tools. The broader list below also accommodates the restaurant and tutor test cases and categories already anticipated in this library; it is not a frequency ranking.

| Bucket | When to use it | Typical content |
|---|---|---|
| Problem / Need | The visitor needs help recognizing a problem or its consequences. | Symptoms, frustrations, current limitations. |
| Process / How It Works | The steps to starting or receiving the service need explanation. | Inquiry, consultation, delivery, follow-up. |
| Featured Service / Offer | One service deserves more attention than an overview card. | Detailed explanation, benefits, supporting media, CTA. |
| Pricing / Packages / Funding | Costs, inclusions, or funding options help the visitor decide. | Prices, inclusions, conditions, funding explanation. |
| FAQ / Objections | Common uncertainties can be answered before contact. | Eligibility, timing, cancellation, practical questions. |
| Portfolio / Projects / Case Studies | Actual work provides evidence of capability. | Project images, brief, approach, attributable results. |
| Gallery | Visual experience or atmosphere is central to the offer. | Venue, food, classes, facilities, or work photos. |
| Team / Individual Profile | Choosing the people is part of choosing the service. | Tutor or founder profile, qualifications, team members. |
| Location / Coverage / Visit | Visitors need to know where or when the service is available. | Address, map, service area, opening hours, directions. |
| Booking / Availability / Timetable | The visitor needs to select a time or session. | Lesson availability, class schedule, reservation integration. |
| Menu / Detailed Catalogue / Listings | The offering needs more detail than service cards can hold. | Restaurant menu, course catalogue, property listings. |
| News / Articles / Resources | Useful maintained content supports discovery or understanding. | Recent posts, guides, downloads, educational material. |
| Promotions / Announcements | Temporary information changes the visitor's decision. | Seasonal offer, new course, holiday hours, event notice. |
| Mission / Values / Community | Purpose and community involvement materially explain the business. | Mission, commitments, local initiatives. |
| Interactive Tool / Search | A task benefits from input and a result. | Property search, configurator, eligibility check, calculator. |

## Selection and Boundary Rules

- Choose buckets from site purpose, funnel logic, and real available content. Do not add every section to every page.
- Give each reference one primary bucket; use secondary tags when it serves several purposes instead of duplicating the reference.
- Keep a brief business introduction under About; use Team/Profile for a dedicated people section, and Mission/Community for a dedicated purpose section.
- Use Portfolio/Case Studies for work explained as evidence; use Gallery for visual browsing, and Catalogue/Listings for items visitors select from.
- Use Services for the overview and Featured Service for a dedicated deeper explanation. An offer embedded in either does not automatically require another pricing section.
- CTA/Contact covers the action and contact route; Booking adds scheduling, and Location adds visiting or coverage information.
- Grids, split panels, accordions, and carousels are layouts or interaction patterns within buckets. Video, masks, gradients, and motion are media/design/effects choices, not section buckets.
- An optional section does not automatically make its functionality part of the standard commercial offer. Custom search, booking, calculators, and integrations still require scope and maintenance assessment.
- Build wireframe variants as useful references arrive; this inventory does not imply that implementations already exist.
