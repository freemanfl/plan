# Website Generation Visual Structure Schema

This specification is the contract used to:

1. Scan and describe reference websites consistently.
2. Store reusable design patterns in machine-readable form.
3. Convert customer data into competent website layouts.
4. Generate readable teardown documents and implementation briefs.

It complements [customer-data-schema.md](customer-data-schema.md).

## Core principles

- Store relationships and constraints, not screenshot coordinates.
- Separate structure from decorative finish.
- Define desktop and mobile behavior explicitly.
- Every section must have a purpose.
- Every effect must justify its complexity.
- Asset quality limits visual ambition.
- Preserve factual content separately from generated presentation.
- Prefer simple, robust treatments that create strong perceived quality.

## File format

YAML is the preferred authoring format because it is readable and machine-friendly. JSON may be generated from the same schema.

```yaml
schema_version: "1.0"
document_type: visual_structure
mode: reference_scan # reference_scan | generation_plan
```

## Top-level schema

```yaml
schema_version: "1.0"
document_type: visual_structure
mode: reference_scan

source:
  name: ""
  url: ""
  captured_at: ""
  desktop_viewport: "1440x1000"
  mobile_viewport: "390x844"
  screenshots:
    desktop: ""
    mobile: ""

classification:
  business_category: ""
  visual_style: conventional
  market_level: mid
  content_density: medium
  image_dependency: medium
  implementation_complexity: low

architecture: {}
design_system: {}
responsive_system: {}
motion_system: {}
sections: []
evaluation: {}
```

## Allowed classification values

### Visual style

- `conventional`: familiar marketing-site structure
- `editorial`: typography and image sequencing resembling a publication
- `image_led`: photography carries most of the communication
- `product_led`: interface or product demonstrations dominate
- `conversion_led`: offers, proof, and CTAs dominate
- `experimental`: deliberately broken grids, navigation, or interaction

Multiple values may be stored when necessary, but one must be marked primary.

### Market level

- `budget`
- `accessible`
- `mid`
- `premium`
- `luxury`

### Content density

- `sparse`
- `low`
- `medium`
- `high`
- `very_high`

### Dependency and complexity

- `low`
- `medium`
- `high`
- `specialist`

## Architecture schema

```yaml
architecture:
  page_type: homepage
  page_goal: generate_consultation_leads
  primary_conversion: book_consultation
  secondary_conversion: view_services

  header_behavior: sticky
  footer_depth: standard
  homepage_length: medium

  navigation:
    depth: 1
    desktop_pattern: horizontal
    mobile_pattern: drawer
    primary_items: 5
    utility_items: 1
    persistent_cta: true

  section_sequence:
    - navigation
    - hero
    - trust_strip
    - services
    - how_it_works
    - testimonials
    - faq
    - final_cta
    - footer
```

### Architecture values

`header_behavior`:

- `static`
- `sticky`
- `sticky_after_scroll`
- `overlay`
- `hidden_until_scroll_up`

`footer_depth`:

- `minimal`
- `standard`
- `directory`

`homepage_length`:

- `short`: 3–5 primary sections
- `medium`: 6–9 primary sections
- `long`: 10 or more primary sections

`desktop_pattern`:

- `horizontal`
- `centered_logo`
- `split_navigation`
- `sidebar`
- `menu_overlay`

`mobile_pattern`:

- `drawer`
- `full_screen_overlay`
- `accordion_drawer`
- `bottom_navigation`
- `simplified_links`

## Global design system

```yaml
design_system:
  layout:
    viewport_model: fluid_with_max_width
    content_max_width: 1200px
    reading_max_width: 680px
    wide_max_width: 1440px
    desktop_columns: 12
    desktop_gutter: 24px
    mobile_columns: 4
    mobile_gutter: 16px
    page_padding_desktop: 32px
    page_padding_tablet: 24px
    page_padding_mobile: 20px

  spacing:
    base_unit: 4px
    section_gap_desktop: 112px
    section_gap_mobile: 64px
    component_gap: 24px
    text_gap: 16px

  typography:
    heading_class: humanist_sans
    body_class: neutral_sans
    accent_class: none
    scale_ratio: 1.25
    h1_desktop: 64px
    h1_mobile: 42px
    body_desktop: 18px
    body_mobile: 16px
    heading_weight: 650
    body_weight: 400
    heading_line_height: 1.05
    body_line_height: 1.55
    heading_letter_spacing: -0.03em
    alignment_default: left

  color:
    mode: light
    background: "#F7F5F0"
    surface: "#FFFFFF"
    text_primary: "#17201A"
    text_secondary: "#59615B"
    accent: "#E85D3F"
    accent_text: "#FFFFFF"
    border: "#DDDCD7"
    semantic_success: "#247A48"
    contrast_level: high

  shape:
    corner_character: soft
    radius_small: 8px
    radius_medium: 14px
    radius_large: 24px
    radius_pill: 999px
    border_width: 1px

  elevation:
    default: subtle
    card_shadow: "0 8px 30px rgba(0,0,0,0.08)"
    floating_shadow: "0 18px 60px rgba(0,0,0,0.14)"

  imagery:
    treatment: natural
    crop_character: human
    default_radius: 20px
    overlay_strength: 0
    color_grade: warm_neutral

  buttons:
    height: 48px
    horizontal_padding: 24px
    radius: 10px
    primary_style: filled
    secondary_style: outline
    label_weight: 600
```

### Typography classes

- `neutral_sans`
- `humanist_sans`
- `geometric_sans`
- `grotesk`
- `editorial_serif`
- `traditional_serif`
- `display_serif`
- `monospace`
- `handmade`

### Corner character

- `square`
- `slightly_soft`
- `soft`
- `rounded`
- `pill_heavy`
- `mixed`

### Image treatment

- `natural`
- `editorial`
- `high_contrast`
- `muted`
- `monochrome`
- `duotone`
- `cutout`
- `collage`
- `framed`
- `full_bleed`

## Responsive system

```yaml
responsive_system:
  breakpoints:
    mobile: 0px
    tablet: 768px
    desktop: 1024px
    wide: 1440px

  type_scaling: clamp
  spacing_scaling: stepped
  mobile_priority: conversion_first

  defaults:
    multicolumn_behavior: stack
    card_grid_behavior: "3_to_2_to_1"
    image_position_when_stacked: after_content
    navigation_behavior: drawer
    button_behavior: full_width_when_needed
    decorative_asset_behavior: hide_if_crowded

  accessibility:
    minimum_touch_target: 44px
    respects_reduced_motion: true
    keyboard_navigation_required: true
    visible_focus_required: true
    minimum_body_text_mobile: 16px
```

## Motion system

```yaml
motion_system:
  overall_level: restrained
  complexity_budget: low
  performance_budget: low

  durations:
    quick: 160ms
    standard: 280ms
    entrance: 480ms
    ambient: 8000ms

  easing:
    standard: "cubic-bezier(0.2, 0.8, 0.2, 1)"
    entrance: "cubic-bezier(0.16, 1, 0.3, 1)"

  allowed_defaults:
    - button_state_change
    - card_hover_lift
    - fade_up_on_entry
    - accordion_expand
    - image_scale_on_hover

  avoid_by_default:
    - scroll_hijacking
    - continuous_cursor_effects
    - webgl_distortion
    - excessive_parallax
    - long_page_load_sequences

  reduced_motion:
    remove_parallax: true
    remove_large_transforms: true
    retain_short_opacity_changes: true
```

`overall_level`:

- `none`
- `minimal`
- `restrained`
- `expressive`
- `experimental`

## Universal section schema

Every section uses this base structure.

```yaml
- id: unique_section_id
  type: hero
  variant: split_content_media
  order: 1
  purpose: communicate_offer_and_drive_primary_conversion
  source_content: []
  content: {}
  layout: {}
  visual: {}
  motion: {}
  responsive: {}
  analysis: {}
```

### Required section fields

- `id`
- `type`
- `variant`
- `order`
- `purpose`
- `content`
- `layout.desktop`
- `layout.mobile`
- `analysis.visual_emphasis`
- `analysis.implementation_complexity`

### Section types

- `announcement_bar`
- `navigation`
- `hero`
- `trust_strip`
- `introduction`
- `problem`
- `benefits`
- `services`
- `featured_service`
- `process`
- `about`
- `team`
- `results`
- `testimonials`
- `case_studies`
- `gallery`
- `pricing`
- `locations`
- `schedule`
- `faq`
- `contact`
- `newsletter`
- `final_cta`
- `footer`
- `custom`

## Layout primitive schema

```yaml
layout:
  desktop:
    section_width: full
    min_height: 720px
    max_height: none

    container:
      max_width: 1200px
      padding_inline: 32px
      padding_block: 96px

    grid:
      columns: 12
      gap: 32px
      row_gap: 32px
      vertical_alignment: center

    regions:
      content:
        column_start: 1
        column_span: 5
        alignment: left
      media:
        column_start: 7
        column_span: 6
        alignment: center

    content_order:
      - eyebrow
      - heading
      - description
      - actions
      - trust_note

    spacing:
      eyebrow_to_heading: 16px
      heading_to_description: 24px
      description_to_actions: 32px
      actions_to_trust: 20px

  mobile:
    section_width: full
    min_height: auto

    container:
      padding_inline: 20px
      padding_block: 56px

    layout_mode: stack
    alignment: left
    gap: 32px

    content_order:
      - eyebrow
      - heading
      - description
      - actions
      - trust_note
      - media
```

### Layout values

`section_width`:

- `full`
- `wide`
- `contained`
- `reading`

`layout_mode`:

- `grid`
- `flex_row`
- `stack`
- `overlay`
- `masonry`
- `carousel`
- `absolute_composition`

`alignment`:

- `left`
- `center`
- `right`
- `start`
- `end`
- `stretch`

## Complete hero example

```yaml
- id: home_hero
  type: hero
  variant: split_content_media
  order: 1
  purpose: communicate_offer_and_drive_primary_conversion

  source_content:
    - business.category
    - business.description
    - audience.primaryCustomer
    - audience.desiredOutcome
    - offer.primaryService
    - offer.differentiator
    - conversion.primaryGoal
    - trust.reviewScore

  content:
    eyebrow:
      text: "Online maths tutoring"
      required: false
    heading:
      text: "Build confidence and improve your maths results"
      element: h1
      max_lines_desktop: 3
      max_lines_mobile: 4
    description:
      text: "One-to-one lessons with qualified tutors matched to each student's goals."
      max_width: 560px
    primary_cta:
      label: "Find a tutor"
      destination: "/tutors"
    secondary_cta:
      label: "How it works"
      destination: "#how-it-works"
    trust_note:
      text: "Rated 4.8 from 2,400 parent reviews"
    media:
      type: image
      asset: "student-with-tutor.webp"
      alt: "Student attending an online maths lesson"
      focal_point: center

  layout:
    desktop:
      section_width: full
      min_height: 720px
      container:
        max_width: 1200px
        padding_inline: 32px
        padding_block: 96px
      grid:
        columns: 12
        gap: 32px
        vertical_alignment: center
      regions:
        content:
          column_start: 1
          column_span: 5
        media:
          column_start: 7
          column_span: 6
      content_order:
        - eyebrow
        - heading
        - description
        - actions
        - trust_note
      spacing:
        eyebrow_to_heading: 16px
        heading_to_description: 24px
        description_to_actions: 32px
        actions_to_trust: 20px

    mobile:
      layout_mode: stack
      container:
        padding_inline: 20px
        padding_block: 56px
      content_order:
        - eyebrow
        - heading
        - description
        - actions
        - trust_note
        - media
      alignment: left
      gap: 32px
      actions:
        direction: column
        buttons_full_width: true
      media:
        width: 100%
        aspect_ratio: "4:3"
        margin_top: 40px

  visual:
    background: "#F5F1E8"
    text_color: "#18211B"
    accent_color: "#E85D3F"
    heading_scale: display
    media:
      aspect_ratio: "5:4"
      border_radius: 20px
      treatment: natural
      shadow: soft_medium
    primary_button:
      style: filled
      size: large
    secondary_button:
      style: outline
      size: large

  motion:
    entry:
      effect: fade_up
      distance: 16px
      duration: 450ms
      stagger: 80ms
      complexity: low
    media:
      effect: subtle_scale_in
      from_scale: 0.98
      duration: 600ms
      complexity: low

  analysis:
    visual_emphasis: primary
    implementation_complexity: low
    asset_dependency: medium
    signature_details:
      - warm off-white background
      - oversized heading
      - asymmetrical 5/6 column split
      - softly rounded photograph
      - review statement beneath actions
    essential_to_recreate:
      - heading-to-image proportion
      - generous vertical spacing
      - clear CTA hierarchy
    safe_to_simplify:
      - entry animation
      - secondary CTA styling
    reusable_for:
      - tutors
      - consultants
      - local service businesses
      - education companies
```

## Hero variants

- `centered_content_media_below`
- `split_content_media`
- `media_content_split`
- `full_bleed_background`
- `text_only`
- `product_interface`
- `search_led`
- `booking_led`
- `collage`
- `editorial_asymmetric`

## Navigation schema

```yaml
- id: primary_navigation
  type: navigation
  variant: logo_left_links_center_cta_right
  order: 0
  purpose: orientation_and_conversion
  content:
    logo: supplied_logo
    links:
      - label: Services
        destination: "/services"
      - label: About
        destination: "/about"
      - label: Reviews
        destination: "/reviews"
      - label: Contact
        destination: "/contact"
    primary_cta:
      label: "Book a consultation"
      destination: "/book"
  layout:
    desktop:
      height: 72px
      behavior: sticky
      distribution: logo_links_actions
    mobile:
      height: 64px
      visible_items:
        - logo
        - menu_toggle
      menu_pattern: drawer
  analysis:
    visual_emphasis: utility
    implementation_complexity: low
```

Navigation variants:

- `logo_left_links_center_cta_right`
- `logo_left_links_right`
- `centered_logo_split_links`
- `minimal_logo_menu`
- `transparent_overlay`
- `sidebar`

## Services schema

```yaml
- id: services_overview
  type: services
  variant: featured_plus_grid
  order: 3
  purpose: explain_and_prioritize_offers
  content:
    eyebrow: "Services"
    heading: "Support built around your goals"
    description: ""
    featured_service: service_01
    services:
      - service_02
      - service_03
      - service_04
  layout:
    desktop:
      container_max_width: 1200px
      featured_columns: "7:5"
      secondary_grid_columns: 3
      gap: 24px
    mobile:
      layout_mode: stack
      card_grid_columns: 1
  visual:
    card_style: bordered
    image_position: top
    equal_card_heights: true
  analysis:
    visual_emphasis: secondary
    implementation_complexity: low
```

Services variants:

- `equal_card_grid`
- `featured_plus_grid`
- `alternating_rows`
- `compact_icon_list`
- `image_tiles`
- `accordion`
- `filterable_catalogue`

## Process schema

```yaml
- id: how_it_works
  type: process
  variant: numbered_horizontal_steps
  order: 4
  purpose: reduce_uncertainty
  content:
    heading: "How it works"
    steps:
      - number: "01"
        title: "Tell us what you need"
        description: ""
      - number: "02"
        title: "Choose the right option"
        description: ""
      - number: "03"
        title: "Book and get started"
        description: ""
  layout:
    desktop:
      columns: 3
      connector: line
    mobile:
      layout_mode: stack
      connector: vertical_line
  analysis:
    visual_emphasis: supporting
    implementation_complexity: low
```

Process variants:

- `numbered_horizontal_steps`
- `numbered_vertical_steps`
- `alternating_timeline`
- `sticky_explanation`
- `visual_walkthrough`

## Testimonials schema

```yaml
- id: customer_testimonials
  type: testimonials
  variant: featured_quote_plus_cards
  order: 6
  purpose: establish_trust
  content:
    heading: "What customers say"
    rating:
      value: 4.9
      count: 218
      source: Google
    featured_testimonial: testimonial_01
    testimonials:
      - testimonial_02
      - testimonial_03
  layout:
    desktop:
      featured_span: 7
      cards_span: 5
    mobile:
      layout_mode: stack
      overflow_behavior: none
  visual:
    quote_size: large
    attribution_style: name_role_photo
  analysis:
    visual_emphasis: secondary
    implementation_complexity: low
```

Testimonials variants:

- `single_featured_quote`
- `equal_card_grid`
- `featured_quote_plus_cards`
- `carousel`
- `rating_plus_quotes`
- `case_study_preview`

## Gallery schema

```yaml
- id: work_gallery
  type: gallery
  variant: asymmetric_grid
  order: 4
  purpose: demonstrate_quality_visually
  content:
    heading: "Selected work"
    items: asset_collection_selected_work
  layout:
    desktop:
      grid_pattern: "2_1_1"
      row_height: 360px
      gap: 16px
    mobile:
      layout_mode: stack
      aspect_ratio: "4:3"
      item_limit_initial: 6
  visual:
    captions: on_hover
    image_radius: 8px
  analysis:
    visual_emphasis: primary
    implementation_complexity: medium
```

Gallery variants:

- `uniform_grid`
- `asymmetric_grid`
- `masonry`
- `horizontal_reel`
- `full_width_sequence`
- `project_index`
- `before_after`

## FAQ schema

```yaml
- id: frequently_asked_questions
  type: faq
  variant: two_column_accordion
  order: 7
  purpose: resolve_objections
  content:
    eyebrow: "Questions"
    heading: "Everything you need to know"
    items: faq_collection
  layout:
    desktop:
      intro_span: 4
      accordion_span: 7
      gap_span: 1
    mobile:
      layout_mode: stack
  motion:
    accordion:
      effect: height_and_opacity
      duration: 240ms
      complexity: low
  analysis:
    visual_emphasis: supporting
    implementation_complexity: low
```

FAQ variants:

- `single_column_accordion`
- `two_column_accordion`
- `categorized_accordion`
- `simple_question_list`

## Final CTA schema

```yaml
- id: final_conversion
  type: final_cta
  variant: contained_banner
  order: 8
  purpose: close_the_page_with_one_action
  content:
    heading: "Ready to get started?"
    description: "Book an introductory consultation."
    primary_cta:
      label: "Book a consultation"
      destination: "/book"
    reassurance: "No obligation. Response within one business day."
  layout:
    desktop:
      alignment: center
      max_width: 1200px
      padding_block: 80px
    mobile:
      alignment: left
      padding_block: 56px
      button_full_width: true
  analysis:
    visual_emphasis: primary
    implementation_complexity: low
```

Final CTA variants:

- `contained_banner`
- `full_width_band`
- `split_content_action`
- `image_backed`
- `contact_form`
- `booking_embed`

## Footer schema

```yaml
- id: global_footer
  type: footer
  variant: standard_multicolumn
  order: 9
  purpose: utility_navigation_and_business_identity
  content:
    identity:
      logo: supplied_logo
      description: business.shortDescription
    columns:
      - label: Services
        links: service_links
      - label: Company
        links: company_links
      - label: Contact
        links: contact_links
    legal_links:
      - privacy
      - terms
    social_links: supplied_social_links
  layout:
    desktop:
      columns: "5_2_2_3"
    mobile:
      layout_mode: stack
      link_groups: accordion_optional
  analysis:
    visual_emphasis: utility
    implementation_complexity: low
```

Footer variants:

- `minimal`
- `standard_multicolumn`
- `directory`
- `newsletter_led`
- `location_led`

## Section analysis schema

Every scanned section must contain:

```yaml
analysis:
  visual_emphasis: primary
  implementation_complexity: low
  asset_dependency: medium
  content_dependency: medium

  signature_details: []
  essential_to_recreate: []
  safe_to_simplify: []
  expensive_or_fragile: []
  low_cost_equivalent: []
  reusable_for: []
```

`visual_emphasis`:

- `primary`
- `secondary`
- `supporting`
- `utility`

## Reference scan observations

Measurements captured from references may be approximate, but confidence must be recorded.

```yaml
observation:
  measurement_method: visual_estimate
  confidence: medium
  desktop_verified: true
  mobile_verified: true
  dynamic_content_present: false
  inaccessible_details: []
```

`measurement_method`:

- `computed`
- `browser_inspection`
- `screenshot_measurement`
- `visual_estimate`

`confidence`:

- `low`
- `medium`
- `high`

## Required QA validation

### Document-level checks

- A source URL and capture date exist for reference scans.
- A business category and primary visual style are assigned.
- Desktop and mobile viewports are recorded.
- Section sequence matches the recorded sections.
- Every section has a unique ID and explicit purpose.
- The primary conversion action remains consistent.
- Global design values are not needlessly repeated inside sections.
- Unknown values are marked unknown rather than invented.

### Layout checks

- Desktop column spans do not exceed the grid.
- Section order is explicit.
- Mobile order is explicit when it differs from desktop.
- Text widths are constrained for readability.
- Images include aspect ratio and focal-point behavior.
- Full-bleed elements identify how they escape the container.
- Overlapping elements identify their anchor and stacking order.
- Absolute composition includes a conventional mobile fallback.

### Content checks

- Every displayed fact maps to a customer-data source.
- H1 is unique and reflects the primary offer.
- CTA labels describe the action.
- Testimonials and statistics have supplied sources.
- Missing content causes omission or fallback, never fabrication.

### Responsive checks

- Navigation has a mobile pattern.
- Multi-column layouts define their stack order.
- Touch targets are at least 44px.
- Mobile body text is at least 16px.
- Horizontal overflow is intentional and documented.
- Decorative media may be removed without losing meaning.

### Motion checks

- Every effect has a purpose.
- Complexity and performance cost are recorded.
- Reduced-motion behavior exists.
- Interaction does not hide required content.
- High-cost effects include a low-cost equivalent.

### Practicality checks

- Complexity matches the client level and budget.
- Visual ambition matches asset quality.
- No section is decorative without supporting comprehension, trust, or conversion.
- Signature details are limited to the smallest set producing the intended character.
- The page remains competent with motion disabled.

## Generated human-readable teardown

The structured data should generate a document with this order:

1. Site identity and classification
2. Full-page skeleton
3. Global layout and design system
4. Desktop and mobile wireframes
5. Section-by-section breakdown
6. Typography, color, imagery, and components
7. Motion and interaction
8. Signature details
9. Complexity and low-cost equivalents
10. Reusable patterns
11. QA notes and uncertain observations

## Relationship to customer data

The customer-data schema answers:

> What true information and assets do we have?

The visual-structure schema answers:

> How should that information and those assets be arranged, emphasized, styled, and adapted?

The generator must never use the visual schema to invent missing customer facts.
