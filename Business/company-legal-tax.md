# Web Studio — Company, Legal & Tax Setup (Czech Republic)

## Purpose

This document covers the business-entity and compliance side of the Web Studio in the Czech Republic.

It is intentionally separate from the Master Plan, Offer / Service Scope, Technical Services, Sales, Design / Layout, and Maintenance Automation.

This file should answer practical questions such as:
- How do we legally start operating?
- Should the business begin as OSVČ or s.r.o.?
- What registrations are required?
- What taxes and insurance payments apply?
- When does VAT become relevant?
- What must appear on invoices?
- What recurring filings and deadlines exist?
- What payment/banking setup is sensible?

Because Czech tax and social-insurance rules change frequently, all numerical thresholds and contribution amounts must be treated as time-sensitive and re-verified before acting on them.

---

# 1. Likely Starting Form

## 1.1 OSVČ / živnostník

For a solo founder testing a small web studio, the simplest initial structure is generally **OSVČ (self-employed individual / živnostník)**.

Main reasons:
- simple and cheap to establish;
- relatively little administration;
- suitable for solo service work;
- easy to invoice clients;
- can accept online/card payments;
- can later transition to an s.r.o. if scale, liability, tax planning, hiring, or branding makes that worthwhile.

For the Web Studio, likely activities include website development, programming, graphic/web design, marketing-related services, hosting/support, and similar IT/business services.

The exact živnost categories should be confirmed at registration, but much of this type of work is typically covered by **volná živnost** rather than a regulated trade requiring professional qualification.

## 1.2 s.r.o.

An **s.r.o.** may become useful later if:
- the business has meaningful recurring revenue;
- multiple people become formally involved;
- liability separation becomes important;
- larger clients prefer dealing with a company;
- profit retention/tax planning makes it worthwhile;
- the founder wants a separate legal entity and brand.

Do not create an s.r.o. merely because it sounds more professional. For an early solo test, the administrative overhead may not yet be justified.

---

# 2. Opening the Business

## 2.1 Basic OSVČ setup

Typical startup sequence:

1. Decide the business activities / živnost scope.
2. Register the trade through the Czech Trade Licensing Office / online registration system.
3. Receive the IČO.
4. Ensure registration/notification with:
   - tax administration where required;
   - Czech Social Security Administration (ČSSZ);
   - health insurance company.
5. Set up invoicing.
6. Set up a business/payment account structure.
7. Decide expense method and accounting/tax-record approach.
8. Verify whether VAT registration or another cross-border VAT obligation applies.
9. Begin contracting/invoicing clients.

The Czech unified registration process can handle several startup notifications in one workflow.

---

# 3. Main Activity vs Side Activity

For social-security purposes, OSVČ activity may be treated as **main (hlavní)** or **secondary (vedlejší)** depending on circumstances such as employment, studies, pension, parental status, etc.

This matters materially because:
- minimum social-security obligations differ;
- a secondary activity can have substantially lighter initial contribution requirements;
- thresholds determine when pension-insurance participation becomes mandatory.

The Web Studio document should eventually record the founder's actual status at launch and calculate obligations from that status rather than assuming "main OSVČ."

---

# 4. Income Tax

## 4.1 Standard income-tax route

OSVČ pays Czech personal income tax on the applicable tax base.

The business must decide how expenses are handled, normally through either:
- actual documented expenses; or
- an allowed lump-sum expense percentage (výdajový paušál), if applicable to the relevant activity.

The best method depends on:
- revenue;
- real operating costs;
- applicable expense percentage;
- other taxable income;
- tax credits/allowances;
- VAT situation.

This should be modeled before launch rather than choosing a method by habit.

## 4.2 Paušální daň

The Czech **paušální režim / flat-tax regime** may simplify administration for eligible OSVČ by combining income tax, social insurance, and health insurance into one regular payment.

It is not automatically the cheapest option.

Before choosing it, compare:
- normal tax + expense allowance;
- social insurance;
- health insurance;
- available deductions/credits;
- expected annual revenue;
- any employment income;
- VAT status and eligibility restrictions.

---

# 5. Social Insurance — 2026 Notes

Social-security figures are time-sensitive.

As of July 2026, ČSSZ states the minimum monthly social-security advance for a main OSVČ is **5,005 CZK**.

For a person starting main self-employment who did not perform self-employment in the preceding 20 calendar years, the special reduced minimum advance is **3,575 CZK** in 2026.

ČSSZ also notes a separate rule under which some newly starting/restarting OSVČ who had not performed self-employment in the preceding five calendar years can be exempt from paying advances during the start period, with final liability settled through the annual statement. The exact interaction of the startup exemptions/minimum rules must be checked against the founder's actual history before launch.

For secondary activity, 2026 rules differ and may mean no advances in the first year, subject to the annual profit/assessment threshold.

### Action rule

Do **not** hard-code one social-security number into the business model.

At launch, determine:
- main vs secondary activity;
- prior OSVČ history;
- start date;
- applicable minimum;
- whether advance exemption applies.

---

# 6. Health Insurance

Health-insurance obligations must be registered with the founder's Czech health insurer.

The applicable minimum advances depend on:
- whether self-employment is main or secondary;
- employment status;
- statutory exceptions;
- annual assessment base.

The exact current 2026 minimum and launch treatment should be verified with the founder's insurer immediately before registration.

The business should keep a small compliance table containing:
- insurer;
- payment account;
- variable symbol;
- monthly advance;
- due date;
- last annual statement filed.

---

# 7. VAT / DPH

VAT needs its own check before the studio begins selling broadly.

Questions to answer:
- Is the business below the Czech mandatory VAT-registration threshold?
- Are Czech clients being served only?
- Are services being sold to EU businesses?
- Are services being sold to EU consumers?
- Are services being bought from foreign platforms/providers?
- Does the studio become an **identified person (identifikovaná osoba)** even while not being a full VAT payer?
- Will Stripe, hosting, SaaS, advertising, or other foreign services create VAT reporting obligations?

Important: a business can have EU VAT-related obligations **without being a normal Czech VAT payer**.

Before accepting cross-border EU business, this should be checked carefully.

---

# 8. Invoicing

Invoices should be generated consistently and stored.

Typical information:
- legal name / entrepreneur name;
- business address;
- IČO;
- DIČ if applicable;
- invoice number;
- issue date;
- taxable-supply/payment date where applicable;
- customer details;
- description of service;
- amount/currency;
- payment instructions;
- VAT information where relevant.

Use sequential invoice numbering and keep records in one system.

A simple invoicing tool is preferable to manually editing PDFs.

---

# 9. Contracts / Terms

Even with a simple one-offer product, the studio needs written commercial terms.

At minimum define:
- what the subscription/service includes;
- what counts as normal maintenance;
- what is custom/out-of-scope work;
- payment timing;
- late/non-payment;
- cancellation;
- ownership and client exit;
- hosting/domain responsibility;
- third-party services;
- client-supplied content;
- liability limits;
- privacy/data processing;
- reasonable support response expectations.

The contract should mirror the Offer & Service Scope document rather than inventing a different promise.

---

# 10. Banking & Payments

A separate business account is strongly preferable even if not always legally mandatory for an OSVČ.

Benefits:
- clean bookkeeping;
- easier tax preparation;
- easier Stripe/payment-provider reconciliation;
- clearer separation of personal and business money.

Potential payment channels:
- Czech/EU bank transfer;
- Stripe/card payments;
- recurring subscription payments;
- payment links/invoices.

Before using Stripe or another gateway:
- verify OSVČ onboarding requirements;
- ensure business name/website/contact information is ready;
- understand fees;
- define refund/cancellation handling;
- connect payouts to the business account.

---

# 11. Accounting / Record Keeping

The studio needs a simple system for retaining:
- issued invoices;
- received invoices/receipts;
- SaaS/hosting bills;
- payment-provider statements;
- bank statements;
- client contracts;
- tax filings;
- social/health annual statements.

Likely operating costs include:
- hosting;
- domains;
- AI/API usage;
- SaaS;
- payment processing;
- advertising;
- software;
- subcontractors;
- accountant/tax adviser.

Do not let recurring software purchases become untracked personal-card expenses.

---

# 12. Recurring Compliance Checklist

## Monthly
- reconcile incoming client payments;
- save business expenses/invoices;
- pay required social advance;
- pay required health advance;
- handle VAT/identified-person reporting if applicable;
- review overdue client invoices.

## Annually
- personal income-tax return;
- ČSSZ income/expense statement;
- health-insurance income/expense statement;
- reconcile tax/social/health balances;
- update advances for the new year;
- review VAT status;
- review whether OSVČ still makes sense versus s.r.o.

---

# 13. s.r.o. Migration Trigger

Do not set a rigid revenue threshold yet.

Re-evaluate s.r.o. when several of these become true:
- stable recurring revenue;
- business income materially exceeds side-project level;
- liability exposure rises;
- wife/other people become formal operators/employees;
- subcontracting/hiring grows;
- B2B customers expect a company;
- taxation becomes materially better through a company structure;
- the founder wants to retain profits in the business;
- brand/business may eventually exist independently of the founder.

At that point, compare OSVČ vs s.r.o. using actual numbers with a Czech accountant/tax adviser.

---

# 14. Before Launch — Concrete Checklist

- [ ] Confirm right to conduct self-employment under residence/status conditions.
- [ ] Confirm exact živnost activities.
- [ ] Decide main vs secondary OSVČ status.
- [ ] Register živnost / receive IČO.
- [ ] Confirm ČSSZ registration and correct 2026 advance treatment.
- [ ] Confirm health-insurance registration and advance.
- [ ] Choose normal tax vs paušální režim.
- [ ] Choose actual expenses vs applicable expense allowance.
- [ ] Check VAT / identified-person obligations.
- [ ] Open/separate business bank account.
- [ ] Set up invoicing software and numbering.
- [ ] Set up Stripe/payment collection if desired.
- [ ] Prepare service agreement / terms.
- [ ] Prepare privacy/GDPR documents needed for the studio itself.
- [ ] Set up accounting document storage.
- [ ] Decide whether to use an accountant from day one.

---

# 15. Research / Questions Still Open

- Exact živnost wording/categories for the intended offer.
- Founder-specific main/secondary status.
- Founder-specific social-security startup exemption.
- Exact current health-insurance advance at launch.
- Best expense method for projected revenue/costs.
- Whether paušální daň is advantageous.
- Exact VAT/identified-person treatment for foreign SaaS and EU clients.
- Whether/when an s.r.o. becomes economically worthwhile.
- Accountant choice and expected annual cost.
- Contract/terms review by a Czech lawyer if needed.
