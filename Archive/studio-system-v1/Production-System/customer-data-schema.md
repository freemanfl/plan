# Website Generation Customer Data Schema

This document defines the customer information a website-generation system needs to produce a competent website. It serves as both an intake mold and a QA checklist.

## Core rule

Facts come from structured customer inputs. Copy, hierarchy, layout, and presentation may be generated. Unsupported facts must never be invented.

## Minimum viable brief

The generator should not proceed without these inputs or an explicit decision to omit them.

| Input | Website output |
|---|---|
| Business name | Logo text, navigation, metadata, footer |
| Business category | Page structure and appropriate sections |
| One-sentence description | Hero copy and metadata |
| Primary customer | Language, imagery, and emphasis |
| Primary customer problem | Hero and problem section |
| Main service or offer | Hero, services, and CTA |
| Primary conversion goal | Main CTA throughout the website |
| CTA label | Button copy |
| CTA destination/contact method | Form, booking, phone, email, or checkout |
| Location or service area | Local messaging, contact, and footer |
| Services or products | Service cards and detail sections |
| Differentiator | Value proposition and benefits |
| Available evidence | Testimonials, results, reviews, or credentials |
| Brand personality | Copy tone and visual direction |
| Available imagery | Image-led versus typography-led layout |
| Required pages | Navigation and sitemap |

## 1. Business identity

- Business name
- Short name
- Logo
- Tagline
- Business category
- Short description
- Full description
- Founding year
- Founder or owner name
- Founder story
- Mission
- Values
- Brand personality
- Preferred language
- Formality level
- Words to use
- Words to avoid

## 2. Audience and positioning

- Primary audience
- Secondary audience
- Audience location
- Audience knowledge level
- Main problem
- Desired outcome
- Purchase motivation
- Common objections
- Reasons customers choose the business
- Alternatives or competitors
- Market level
- Price positioning

## 3. Conversion goal

- Primary action
- Primary CTA label
- Primary CTA destination
- Secondary action
- Secondary CTA label and destination
- Conversion method
- Required lead information
- Response expectation
- Availability
- Current promotion
- Promotion deadline

Typical primary actions include reserving a table, booking a consultation, claiming a trial class, checking availability, requesting a quote, ordering online, or starting a free trial.

## 4. Offers, services, and products

For every offer, collect:

- Name
- Short description
- Full description
- Intended customer
- Problem solved
- Desired outcome
- Deliverables or inclusions
- Process
- Duration
- Price
- Price type
- Availability
- Image
- Offer-specific CTA
- Limitations and exclusions

## 5. Proof and trust

- Testimonials
- Customer names, roles, and photos
- Review score
- Review count
- Review platform
- Customer logos
- Case studies
- Before-and-after material
- Measured results
- Awards
- Certifications
- Qualifications
- Years of experience
- Number of customers
- Press mentions
- Partners
- Guarantees
- Safety information

Only supplied and verifiable proof may be displayed.

## 6. Contact and location

- Address
- Service area
- Phone number
- Email address
- Opening hours
- Map or directions link
- Map embed preference
- Parking information
- Accessibility information
- Public-transport information
- Multiple locations
- Social profiles
- Emergency or after-hours contact

## 7. Navigation and pages

- Required pages
- Primary navigation pages
- Secondary pages
- External booking link
- Customer login
- Language selector
- Location selector
- Shop link
- Legal pages
- Preferred navigation labels

Common pages include Home, About, Services, individual service pages, Pricing, Gallery, Team, Testimonials, FAQ, Resources, Contact, Booking, Privacy, and Terms.

## 8. Hero content

The hero is generated from:

| Element | Source |
|---|---|
| Eyebrow | Category, location, credential, audience, or offer |
| H1 | Main offer plus desired outcome |
| Supporting paragraph | Description, audience, and differentiator |
| Primary CTA | Primary conversion goal |
| Secondary CTA | Secondary action |
| Hero visual | Asset library |
| Trust note | Review, guarantee, credential, or result |
| Availability note | Hours, location, or current availability |

A competent default hero contains an eyebrow, H1, one short paragraph, primary CTA, optional secondary CTA, one relevant visual, and an optional trust signal.

## 9. Selectable homepage sections

The system chooses sections based on available content and business needs. It should not include every section automatically.

- Announcement bar
- Navigation
- Hero
- Trust strip
- Introduction
- Problem framing
- Benefits
- Services
- Featured service
- How it works
- About
- Team
- Results
- Testimonials
- Case studies
- Gallery or portfolio
- Pricing
- Locations
- Schedule
- FAQ
- Final CTA
- Contact
- Newsletter
- Footer

## 10. Images and media

For each asset, collect:

- File
- Asset type
- Subject
- Category
- Orientation
- Resolution or quality
- Focal point
- Caption
- Alt text
- Priority
- Permission status
- Mobile suitability

Layout selection should respond to asset quality:

- Few or weak images: typography-led conventional layout
- Several good images: balanced editorial layout
- Excellent portfolio imagery: visual-first layout
- No imagery: restrained graphic elements, illustration, or product UI

## 11. Brand and styling

- Logo files
- Primary and secondary colors
- Background preference
- Brand fonts
- Brand guide
- Desired personality
- Reference websites
- Disliked websites
- Border preference
- Corner style
- Photography style
- Motion tolerance
- Accessibility requirements

Useful personality values include friendly, professional, energetic, calm, playful, technical, editorial, handmade, minimal, established, youthful, and premium.

## 12. Functionality and integrations

- Contact form
- Booking provider
- Payment provider
- Ordering provider
- Class-management system
- Tutor or product search
- Newsletter provider
- CRM
- Customer login
- Ecommerce requirements
- Filters
- Search
- Calendar
- File downloads
- Live chat
- Analytics
- Cookie consent
- Multilingual requirements

## 13. SEO and sharing

- Page titles
- Meta descriptions
- Primary search phrase
- Secondary search phrases
- Geographic target
- Social-sharing image
- Canonical domain
- Business category
- Business hours
- Address
- Price range
- Author information

The system may draft metadata, but factual business and location information must be supplied.

## 14. Legal and operational requirements

- Legal business name
- Registered address
- Privacy policy
- Terms
- Cookie requirements
- Refund policy
- Cancellation policy
- Accessibility statement
- Required disclaimers
- Age restrictions
- Industry-specific disclosures

## Category-specific requirements

### Restaurant

- Cuisine
- Menu and prices
- Address and hours
- Reservations
- Online ordering
- Dietary options
- Food and venue photography
- Group dining
- Delivery or collection
- Multiple locations

### Tutor or education

- Subjects
- Student ages or levels
- Tutor qualifications
- Lesson format
- Price
- Availability
- Learning outcomes
- Trial lesson
- Safeguarding
- Parent or student testimonials

### Dance studio or gym

- Class types
- Levels
- Age groups
- Schedule
- Instructors
- Locations
- Memberships or class prices
- Trial offer
- Booking platform
- What to bring
- Cancellation rules
- Facility photography

### Photographer or visual professional

- Disciplines
- Portfolio categories
- Selected projects
- Location and travel availability
- Services
- Inquiry process
- Client list
- Publications
- Biography
- High-resolution imagery

### General service business

- Services
- Service area
- Target customer
- Process
- Starting price or quote method
- Results
- Testimonials
- Qualifications
- Availability
- Contact method

## Minimum machine-readable object

```json
{
  "business": {
    "name": "",
    "category": "",
    "description": "",
    "location": "",
    "serviceArea": ""
  },
  "audience": {
    "primaryCustomer": "",
    "mainProblem": "",
    "desiredOutcome": ""
  },
  "offer": {
    "primaryService": "",
    "services": [],
    "differentiator": ""
  },
  "conversion": {
    "primaryGoal": "",
    "ctaLabel": "",
    "ctaDestination": ""
  },
  "trust": {
    "testimonials": [],
    "credentials": [],
    "statistics": []
  },
  "brand": {
    "personality": [],
    "colors": [],
    "references": [],
    "motionLevel": "low"
  },
  "assets": {
    "logo": null,
    "images": []
  },
  "contact": {
    "email": "",
    "phone": "",
    "address": "",
    "hours": ""
  },
  "pages": [],
  "integrations": [],
  "legal": {}
}
```

## QA rules

- Do not invent facts, reviews, prices, results, credentials, people, locations, or policies.
- Identify missing required information before generation.
- Omit unsupported sections instead of filling them with generic claims.
- Every section must support comprehension, trust, or conversion.
- Primary CTAs must use one consistent action and destination.
- Content density and visual ambition must match the quality of available assets.
- The generated site must remain useful on mobile without relying on visual effects.
