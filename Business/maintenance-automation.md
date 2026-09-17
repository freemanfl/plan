# Web Studio Maintenance & Automation System

## Purpose

This document defines the post-launch operating system for handling client changes with minimal repetitive human work while preserving human responsibility.

---

## 1. Client Experience

The client should have an extremely simple request channel.

Possible channels:
- email;
- WhatsApp or similar messaging;
- simple web form/dashboard later.

Clients should not need to understand tickets, GitHub, code, deployments, or technical terminology.

---

## 2. Intended Request Pipeline

Target flow:

**Client request → inbox/ticket → AI interpretation → repository/site identification → proposed code/content change → human approval → tests → deploy**

More specifically:
1. Client sends normal-language request.
2. System captures original request.
3. AI classifies the request and checks whether it is in scope.
4. AI identifies the correct site/repository/files.
5. AI prepares the smallest reasonable change.
6. Approval view shows **original client request + AI proposed change/diff**.
7. Human approves, denies, or escalates.
8. Automated checks run.
9. Change deploys.
10. Request is closed/logged.

---

## 3. Human Roles

### Routine approver
Could eventually be the user's wife or another non-developer operator.

The approval interface should be understandable without coding knowledge.

Expected actions:
- approve;
- reject;
- ask AI to revise;
- escalate to technical owner.

### Technical owner
Handles:
- unusual bugs;
- integrations;
- risky changes;
- infrastructure failures;
- anything AI/operator cannot safely resolve.

---

## 4. GitHub / Version Control

GitHub should serve as:
- source of truth for code;
- AI workspace;
- diff/review surface;
- rollback/history mechanism;
- deployment trigger where appropriate.

Do not assume GitHub Pages is the commercial hosting platform. Static hosting can still be nearly free through appropriate commercial-friendly infrastructure.

---

## 5. Good Automation Candidates

Likely routine requests:
- change opening hours;
- update price;
- replace image;
- add service;
- edit copy;
- change contact information;
- add small banner/notice;
- fix typo;
- update staff/member entry;
- update simple gallery content.

These are ideal because they are bounded and easy to review.

---

## 6. Escalation / Manual Work

Escalate when:
- request changes the design direction substantially;
- new custom functionality is needed;
- third-party integration/API is involved;
- change is ambiguous;
- legal/privacy impact exists;
- AI modifies too many files;
- tests fail;
- request appears outside included maintenance scope.

---

## 7. Scope Protection

Automation does not solve bad scope.

The system must distinguish:
- normal maintenance;
- custom paid work;
- unsupported/risky requests.

Client filtering and scope boundaries are part of keeping maintenance economical.

---

## 8. Core Metric

The important scaling metric is not hosting or AI cost alone.

It is:

**human attention per client per month**

Target direction:
- routine maintenance becomes approval-heavy rather than implementation-heavy;
- founder handles exceptions, not every edit;
- revenue grows faster than founder attention.
