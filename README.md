# Systems Notes

A personal repository for studying algorithms, system programming, operating systems, storage, and computer architecture. I write these notes primarily so I can **come back later and understand what I learned**.

## Language and organization

**README files, directory names, categories, tags, and other metadata are in English. Article titles, summaries, and main text are in Korean.** Keep technical terms, identifiers, code and paper titles in their original language when that is clearer.

| Area | Focus |
| --- | --- |
| [Algorithms](notes/algorithms/) | Data structures, coding interviews, complexity, mistakes and counterexamples |
| [System Programming](notes/system-programming/) | C/C++, POSIX, processes, threads, IPC, files and sockets |
| [Undergraduate Courses](notes/undergraduate/) | OS, computer architecture, networking, databases and digital systems |
| [Linux Kernel](notes/linux-kernel/) | Scheduling, memory, tracing and drivers |
| [Storage & File Systems](notes/storage/) | VFS, EXT4/F2FS, NVMe, flash, persistent I/O |
| [Graduate Study](notes/graduate/) | Upcoming KAIST classes, paper reading, reproducible experiments |

Explanations live in [`notes/`](notes/); runnable implementations and tests live in [`labs/`](labs/). A [study roadmap](notes/study-roadmap.mdx) describes topics to work through, **not work already completed**.

## Writing a note

1. Copy the [concept](notes/_templates/note.mdx), [algorithm](notes/_templates/algorithm.mdx) or [experiment](notes/_templates/experiment.mdx) template into an appropriate topic directory.
2. Write the `title`, `description` and article body in Korean. Use English for `area`, `category`, `type`, `tags` and a unique `study-` slug.
3. Keep `draft: true` and `reviewed: false` while writing.
4. Check accuracy, references and disclosure risk before setting `draft: false`, `reviewed: true`, `sensitivity: public`.
5. Push the change. A website build imports reviewed, public notes.

See [writing guidelines](docs/WRITING.md) for details.

> **Public repository:** Draft notes are visible on GitHub even when they are not published on the website. Never add confidential military infrastructure details, private lab material, personal data, credentials, copyrighted course content or secrets.

## Website integration

The website at [petooooo.github.io/notes/](https://petooooo.github.io/notes/) reads this repository at build time. A scheduled GitHub Actions workflow refreshes the imported notes approximately hourly; the schedule can be delayed. You can trigger the website's deployment workflow manually for a faster update.

**Edit study notes here**, not in the website source. Change the website repository only for presentation, navigation, the CV or engineering portfolio content.
