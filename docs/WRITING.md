# Writing and publication

This repository has two layers: **study notes** in `notes/` and **implementations** in `labs/`. Only a selected, reviewed subset of notes is mirrored to the personal website. Code in `labs/` remains available directly on GitHub.

## Writing a note

1. Choose a topic directory (algorithms, system-programming, undergraduate, linux-kernel, storage, graduate).
2. Copy [`notes/_templates/note.mdx`](../notes/_templates/note.mdx) into that directory with a descriptive file name.
3. Use a unique `slug` starting with `study-`. Keep original source links and distinguish what a reference claims from what you actually tested.
4. Start with `draft: true` and `reviewed: false`.
5. Before publishing, remove sensitive or licensed content, verify code/examples, and update `date`, `area` and `description`.
6. Set all three fields explicitly: `draft: false`, `reviewed: true`, `sensitivity: public`. Commit and push.

The website import script requires all three publication fields and the `study-` slug prefix. The repository's validation workflow checks note metadata and slug uniqueness.

**Caution:** Draft status only hides an article from the website. Every file pushed to this **public** repository is visible on GitHub.

## Learning logs

Useful structure for a topic: question → mental model → code or example → observations → mistakes and limitations → references. For coding tests, additionally record the problem ID/source, complexity, counterexamples, and the actual solution path. For systems experiments, record OS/kernel version, build command, test environment and measurements.

Avoid presenting course coverage, unfinished exercises or intended research as completed results.

## Website synchronization

The Astro website lives in a separate repository. Its GitHub Actions workflow checks out this public repository, imports reviewed notes into a generated directory, and deploys the website. It also runs on an hourly schedule; GitHub's scheduler can occasionally be delayed. For immediate site updates, manually trigger the website's `Deploy GitHub Pages` workflow.

The source-of-truth remains here; generated copies in the website build are not committed.
