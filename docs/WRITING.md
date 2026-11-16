# Editorial and publishing guide

This repository stores **reusable study explanations**, not only short summaries of subjects. A reader should be able to revisit a note months later and reconstruct the key reasoning without reopening a course recording.

## Language contract

- **English:** README files, directory names, repository documentation, metadata labels (`area`, `category`, `type`, `series`, `tags`), slugs, and other navigation.
- **Korean:** Study article title, description, headings, body, examples, explanations, and conclusions.
- **Keep original names:** Commands, APIs, code, identifiers, paper titles, standards, units, proper nouns and terms when translation would obscure their meaning.

Metadata keys themselves remain English. Every published article uses a unique lower-case `study-...` slug.

## Note structure: long-form technical study

For substantial topics, aim for an organized, reference-quality note instead of a few paragraphs. The exact length should follow complexity, but a mechanism-rich tutorial should usually contain:

1. **Motivation:** What question or confusion prompted this note?
2. **Terminology:** Precise definitions and layers involved.
3. **Mechanism:** Step-by-step operations, state transitions, or data flow.
4. **Example:** Small code snippet, scenario or table, clearly labeled if illustrative.
5. **Failure modes:** Where assumptions break, common mistakes and debugging signals.
6. **Trade-offs:** Why one mechanism is chosen over another.
7. **Observability:** What would prove or disprove an explanation?
8. **Reproduction:** OS/kernel versions, setup, commands and actual results where available.
9. **Open questions:** What remains unverified or should be tried next?
10. **Review summary:** Important distinctions and links to related notes.
11. **References:** Primary documentation, papers, and sources.

Tables and images should clarify the mechanism; do not pad an article with decorative graphics. Prefer clean versioned SVGs and properly identified source diagrams.

## Distinguish learning, execution and evidence

- **Studied in a course:** Explain what was learned and why it matters.
- **Illustrative example:** Clearly identify code written to clarify a concept.
- **Executed lab:** Include environment, exact commands, observed output and checks.
- **Measured performance:** Include baseline, workload, repeat count and limitations.
- **Unresolved investigation:** State the observed symptom, hypotheses, actions and open questions.

A course syllabus and conceptual examples are useful sources, but do not fabricate personally executed experiments, benchmark output, kernel patch history, or completed capstones.

## Note metadata

A typical public note:

```yaml
---
title: "한국어 제목"
description: "한국어 설명"
date: "2026-11-15"
draft: false
reviewed: true
sensitivity: public
slug: "study-your-topic"
area: "Linux Kernel"
category: "Study"
type: "concept"
series: "Example Series"
tags: ["linux", "filesystem", "tracing"]
---
```

Drafts remain visible in GitHub and are excluded only from the website importer.

## Workflow

1. Create/edit the source under `notes/`.
2. Run `python3 scripts/validate-notes.py`.
3. Review Markdown links, exact technical terms and citations.
4. Keep internal, personal, military and unpublished lab information out of public content.
5. Commit and push to `main`.
6. Let the website import validated public notes on its next build.
7. Verify the published route `/notes/<slug>/`.

Store runnable code and results under `labs/`; conceptual notes can link to lab repositories or reproducible outputs.

## Study roadmap maintenance

The [kernel-to-storage reading guide](../notes/study-roadmap.mdx) connects topics; the [topic index](../notes/study-curriculum.mdx) links individual articles. Treat technical notes, executed labs, and verified measurements as different kinds of evidence.

## Public safety and disclosure

This is a **public repository**. Do not include secrets, credentials, internal endpoints, private military deployment topology, production recovery commands, classified details, unpublished laboratory research, personal data or copied copyrighted course content.
