# Web Studio Technical Services Checklist

## Purpose and use

A repeatable quality checklist for every site, separate from layout and visual design. This is a starting checklist, not proof that the pipeline already implements it or a change to the commercial offer.

Create a per-site copy. Record URL, reviewed version, date, reviewer, and evidence. Mark items Pass, Fail, or Not applicable with a reason. Unchecked means unverified. Automate routine checks, but retain manual review and human launch approval.

## On-page and local SEO

- [ ] Descriptive page titles, appropriate meta descriptions, and clear heading hierarchy.
- [ ] Useful business/service copy and working descriptive internal links.
- [ ] Accurate, consistent business name, hours, address/service area, and contact details.
- [ ] Appropriate image alternatives; no keyword stuffing or invented claims.
- [ ] Production indexing directives, canonical URLs, redirects, and sitemap checked.
- [ ] Structured data, if used, matches visible facts and is validated.
- [ ] Multilingual pages have correct language declarations and alternate-page relationships where applicable.
- [ ] Search ownership and post-launch indexing follow-up assigned where included.

Reference: [Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide). No guaranteed rankings or indexing; off-page SEO remains outside the initial promise.

## Responsiveness

- [ ] Every page reviewed at narrow mobile, tablet, desktop, and intermediate widths.
- [ ] No unintended overflow, clipped text, overlaps, or broken image crops.
- [ ] Menus, forms, galleries, cards, and sticky elements work on touch screens.
- [ ] Long names, translated text, and missing optional content do not break layouts.
- [ ] Portrait/landscape and agreed mobile/desktop browsers checked, with real-device checks where available.

## Accessibility

Proposed evaluation baseline: [WCAG 2.2 Level AA](https://www.w3.org/TR/WCAG22/). This abbreviated list is not a complete conformance audit. Review all applicable criteria before claiming conformance.

- [ ] Semantic structure, page language, headings, and accessible control names checked.
- [ ] Meaningful image alternatives; decorative images ignored by assistive technology.
- [ ] Full keyboard operation, logical focus order, visible focus, and no traps.
- [ ] Menus/dialogs manage focus; repeated navigation can be bypassed.
- [ ] Applicable text/control contrast requirements met; color is not the only cue.
- [ ] Zoom, text resizing, and reflow preserve content and functionality.
- [ ] Touch targets meet applicable size/spacing requirements; dragging alternatives exist where needed.
- [ ] Forms have labels, instructions, accessible errors, and announced status messages.
- [ ] Reduced-motion preferences respected; moving content has controls where required; no unsafe flashing.
- [ ] Captions, descriptions, and media alternatives provided where applicable.
- [ ] Automated checks plus manual keyboard and screen-reader testing of key journeys completed.

## Performance

- [ ] Images sized and compressed appropriately, with responsive sources where useful.
- [ ] Initial content loads promptly; deferred assets do not delay essential content.
- [ ] Media dimensions reserved to prevent unexpected layout shifts.
- [ ] Fonts, scripts, and embeds reviewed for unnecessary loading cost.
- [ ] Loading, interaction, and visual stability checked under constrained mobile conditions.
- [ ] Signature effects rechecked for performance and usability; simplified if necessary.
- [ ] Post-launch real-user measurements reviewed when available; lab results alone are not sufficient evidence.

## Functionality and content

- [ ] Navigation, calls to action, phone/email links, and booking destinations verified.
- [ ] Forms tested end to end, including actual delivery, invalid input, errors, and success states.
- [ ] Appropriate spam protection and server-side validation implemented where data is processed.
- [ ] Included integrations tested on mobile and desktop, with fallback contact routes.
- [ ] Business facts, prices, translations, images, and usage rights approved.
- [ ] No placeholders, fabricated proof, or unsupported claims remain.
- [ ] Typography, spacing, components, and image treatments are consistent.
- [ ] Effects do not hide information or obstruct controls.

## Deployment and maintenance

- [ ] Domain/DNS/hosting access, ownership, and renewals documented.
- [ ] HTTPS, redirects, error pages, and deployed routes verified.
- [ ] No secrets or private client information exposed in public assets or code.
- [ ] Access permissions, dependencies, and reported security issues reviewed.
- [ ] Rollback is available; required content/data backups have a recovery procedure.
- [ ] Support contact, incident ownership, and appropriate monitoring defined.
- [ ] Production site checked after deployment, not only in preview.

## Privacy and analytics — where applicable

- [ ] Record data collected/transmitted by forms, analytics, embeds, and providers.
- [ ] Obtain appropriate review of notices, consent, retention, and provider responsibilities for the actual setup.
- [ ] Verify implemented data flow and consent behavior match reviewed requirements.
- [ ] Included analytics events verified without unnecessary personal information.

This prompts project-specific review; it is not legal certification or a promise to include every integration.

## Sign-off and later changes

- [ ] Key journeys pass: understand the offer, find business details, contact or book.
- [ ] Failures resolved or documented with an owner and launch decision; serious defects remain blockers.
- [ ] Human approval identifies the exact reviewed version and evidence.
- [ ] Maintenance changes rerun affected checks; shared-component changes receive broader regression review.

## Still to define through testing

- Browser/device matrix and performance acceptance targets.
- Tools, evidence storage, automated checks, and manual responsibilities.
- Full accessibility evaluation process and third-party limitations.
- Which conditional services belong in the standard offer.
