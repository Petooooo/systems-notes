# Systems Notes

Notes on **Linux internals, file systems, storage, system programming, and algorithms**.

I keep explanations and references here, with runnable code and measurements under `labs/`. Published articles also appear on [my website](https://petooooo.github.io/notes/); projects and experience are in the [portfolio](https://petooooo.github.io/projects/).

## Language convention

| Content | Language |
| --- | --- |
| README files, directory names, navigation, documentation | **English** |
| Metadata fields, `slug`, `area`, `category`, `type`, `series`, tags | **English** |
| Study article **titles and descriptions** | **Korean** |
| Study article **explanations and main body** | **Korean** |
| Code, identifiers, commands, standards, paper titles | Original technical language |

Older notes retain their URLs even when the writing is revised.

## Read the notes

| Track | Contents |
| --- | --- |
| [Topic index](notes/study-curriculum.mdx) | Browse articles by subject |
| [Kernel to storage](notes/study-roadmap.mdx) | How processes, memory, file systems and block I/O connect |
| [Linux Systems Foundations](notes/linux-kernel/kdt-overview.mdx) | A six-article learning series on Linux/POSIX, scheduling, VM, VFS, drivers, crash analysis, and observability |
| [System Programming](notes/system-programming/) | POSIX processes, threads, synchronization, IPC, sockets and event-driven I/O |
| [Linux Kernel](notes/linux-kernel/) | Scheduler, memory management, tracing, debugging, interrupt and driver internals |
| [Storage & File Systems](notes/storage/) | VFS, ext4/F2FS, page cache, writeback, block I/O, NVMe, flash and ZNS |
| [Algorithms](notes/algorithms/) | Data structures, patterns, coding-test solutions and complexity analysis |
| [Undergraduate Courses](notes/undergraduate/) | Computer science, computer architecture, networking, digital hardware and related coursework |
| [Graduate Study](notes/graduate/) | Graduate coursework, paper reviews, reproductions, and public research notes |

### Earlier Linux notes

- [Linux internals overview](notes/linux-kernel/kdt-overview.mdx)
- [POSIX programming, IPC and sockets](notes/system-programming/kdt-posix.mdx)
- [Scheduler, virtual memory, VFS and storage](notes/linux-kernel/kdt-kernel-vfs-memory.mdx)
- [Embedded Linux and drivers](notes/linux-kernel/kdt-embedded-linux.mdx)
- [Kernel crash dump analysis](notes/linux-kernel/kdt-crash-dump.mdx)
- [eBPF, BCC, tracing and monitoring](notes/linux-kernel/kdt-ebpf-observability.mdx)

Diagrams used in this series are versioned in [assets/kdt](assets/kdt/), alongside their source articles.

## Repository layout

```text
systems-notes/
├── README.md
├── docs/
│   └── WRITING.md
├── notes/
│   ├── study-curriculum.mdx
│   ├── study-roadmap.mdx
│   ├── linux-kernel/
│   ├── storage/
│   ├── system-programming/
│   ├── algorithms/
│   ├── undergraduate/
│   ├── graduate/
│   └── _templates/
├── assets/
│   ├── roadmap/
│   └── kdt/
├── labs/
│   ├── algorithms/
│   ├── system-programming/
│   ├── kernel/
│   └── storage/
└── scripts/
    └── validate-notes.py
```

**Notes** explain concepts and reasoning. **Labs** contain runnable code, test inputs, measured output and reproducible instructions. A conceptual example in a note is not an assertion that a separate lab was executed.

## Add or revise a note

1. Choose a topic folder under `notes/` and copy a template from [notes/_templates](notes/_templates/).
2. Write `title`, `description`, and the main text in Korean.
3. Use a unique English `study-...` slug and English labels/tags.
4. Include definitions, mechanism, examples, failure cases, confusing distinctions, sources, and your own follow-up questions.
5. Keep `draft: true` and `reviewed: false` until the article is checked.
6. Validate locally with `python3 scripts/validate-notes.py`.
7. Publish with `draft: false`, `reviewed: true`, and `sensitivity: public`.

See [the writing guide](docs/WRITING.md) for the detailed editorial template.

## Website publication

The portfolio's GitHub Actions workflow checks out this repository, validates it, and imports only reviewed public notes at build time. The website is refreshed after portfolio pushes and by a scheduled workflow (approximately hourly, subject to GitHub scheduling delays). A new note should normally be **edited here first**, never copied manually into the website's source.

- Source repository: [Petooooo/systems-notes](https://github.com/Petooooo/systems-notes)
- Website Notes: [petooooo.github.io/notes/](https://petooooo.github.io/notes/)
- Portfolio Projects: [petooooo.github.io/projects/](https://petooooo.github.io/projects/)

> **Disclosure:** This repository is public, including drafts. Do not commit passwords, credentials, internal military infrastructure details, unpublished laboratory materials, non-public data, or copyrighted lecture files. Keep unreviewed sensitive information in a private location.
