# Writing and publishing guidelines

This repository is a learning record, not a place to invent completed experiments or rewrite a course as personal research.

## Language

- **English:** README files, directory names, metadata fields, `area`, `category`, `type`, `tags`, and slugs.
- **Korean:** Article `title`, `description`, body, explanations and conclusions.
- **Original language where appropriate:** Code identifiers, system calls, command output, function names, standards, paper titles and quoted source terms.

## Process

1. Choose the correct topic under `notes/`.
2. Start from a template in `notes/_templates/`.
3. Use a unique lower-case `study-` slug.
4. State the question, your understanding, sources, examples, verified observations and unresolved questions.
5. Use `draft: true` while working. This prevents website publication, **not GitHub visibility**.
6. After review, set `draft: false`, `reviewed: true`, `sensitivity: public`.

The CI validator checks required metadata, date formats, unique slugs and English category labels.

## A useful study note

**Concept:** Question → definition → mechanism → example → confusing points → sources.

**Algorithm:** Problem link → approach → complexity → code → counterexamples → mistakes → takeaway.

**Systems experiment:** OS/kernel and hardware versions → reproducible commands → hypothesis → actual measurements → limitations.

**Paper review:** Research problem → approach → evaluated workload → findings → limitations → your own questions.

Clearly distinguish reading, implementing and measuring. Do not claim a project, kernel patch, benchmark, lab experiment or publication that has not been completed and verified.

## Publication and sensitive information

This repository is **public even for drafts**. Never include internal endpoints, private policies, secrets, military system topology, confidential lab research, unrelated personal data, or copyrighted lecture material. If in doubt, keep the information in a separate private location.

The website imports only entries marked `draft: false`, `reviewed: true`, and `sensitivity: public`. Its generated copies should not be committed manually.
