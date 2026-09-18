# Production pipeline

This is how a site is produced. The idea sits in [README.md](README.md). After launch, looking after the site is a separate loop: [maintenance.md](maintenance.md).

```mermaid
flowchart TD
  gather["1 Gather<br/>raw dump"]
  normalize["2 Normalize<br/>AI cleans text and assets"]
  pack["Standard pack<br/>info + images"]
  structure["3 Structure<br/>AI + category references"]
  style["4 Style<br/>AI + same references"]
  elevate["5 Elevate<br/>human visual pass"]
  site["Site that looks good"]

  gather --> normalize --> pack --> structure --> style --> elevate --> site
```

## 1. Gather

Collect whatever exists: answers, old site, Google listing, Instagram, photos, videos, PDFs, logos.

Do not wait for a perfect brief. The dump can be messy.

Output: a client folder of raw files and notes.

## 2. Normalize — AI, then a human check

AI does the first pass, not the client and not you by hand: clean text, reformat assets, fit what exists into the standard pack, and flag what is missing.

You review that pass. Confirm facts. Decide what to ask the client, generate, or skip.

Output: a standard pack. Later production steps should see this pack, not the raw dump.

The pack itself still has to be distilled from the [references](references.md). See [README.md](README.md).

## 3. Structure

AI proposes sections and order from the pack plus several sites in the matching category. The pool is in [references.md](references.md).

References here answer how this kind of business is explained on a page, not how to copy a brand.

Output: a short page outline (hero, services, proof, contact, and so on) with a job for each section.

## 4. Style

A second pass on the locked outline: type, spacing, color, image treatment, cards, buttons.

Same reference folder, different question: how it should feel. Structure does not get reshuffled here.

Output: a styled implementation of the outline.

## 5. Elevate

A short human pass: crop, spacing, hero, kill anything cheap, one stronger moment if needed.

Time-boxed. If this regularly becomes a full custom-design day, production is not working.

Output: a site that looks good enough to show a client.
