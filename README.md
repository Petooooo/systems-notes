# Systems Notes

A personal study repository for computer science, algorithms, and systems software. The goal is to keep **explanations, experiments, and runnable code** together—not to turn every exercise into a portfolio item.

## Study areas

| Track | What belongs here |
| --- | --- |
| [Algorithms](notes/algorithms/) | Coding tests, data structures, complexity, problem-solving patterns |
| [System programming](notes/system-programming/) | C/C++, POSIX APIs, processes, threads, synchronization, IPC, sockets |
| [Undergraduate subjects](notes/undergraduate/) | Operating systems, computer architecture, networks, databases, digital systems |
| [Linux kernel](notes/linux-kernel/) | Scheduling, virtual memory, tracing, kernel APIs and drivers |
| [Storage](notes/storage/) | VFS, ext4/F2FS, flash/SSD, NVMe, I/O paths |
| [Graduate study](notes/graduate/) | New course notes, paper reading, experiments and research preparation |

**Code and reproducible exercises:** [labs/](labs/) · **Writing rules:** [docs/WRITING.md](docs/WRITING.md)

## How I organize work

- **`notes/`** holds written explanations and learning summaries. Reading or taking a class alone does not imply a completed implementation.
- **`labs/`** holds runnable experiments, coding-test solutions, build instructions, and measurements.
- **Unfinished notes** are drafts. A note is included on [my website](https://petooooo.github.io/notes/) only after I explicitly mark it reviewed and public.
- The source stays here in Git; the website imports approved Markdown/MDX notes during its build. GitHub Actions refreshes the website periodically.

The [study roadmap](notes/study-roadmap.mdx) is an evolving index of topics, not a list of research accomplishments.

## Publishing

Create a Markdown/MDX file using [the template](notes/_templates/note.mdx). Once the content is accurate and safe to share, set `draft: false`, `reviewed: true`, and `sensitivity: public`.

Public GitHub repositories expose **every committed file, including drafts**. Keep lecture recordings, copyrighted course materials, internal infrastructure details, secrets, and private lab work outside this repository.
