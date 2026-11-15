# Systems Notes

알고리즘, 컴퓨터공학 기초, 시스템 프로그래밍, Linux 커널과 스토리지, 대학원 공부를 정리하는 **개인 학습 저장소**다. 다른 사람이 읽는 포트폴리오이기도 하지만, 가장 중요한 목적은 나중에 내가 다시 읽고 이해할 수 있게 공부한 내용을 남기는 것이다.

**글 제목·설명·본문은 한국어**, **카테고리(`area`, `category`)와 태그는 영어**를 기본으로 작성한다. 함수명·시스템 콜·커널 구조체·논문명은 원문 표기를 유지한다.

## 공부 분야

| Category | 정리할 내용 |
| --- | --- |
| [Algorithms](notes/algorithms/) | 자료구조, 시간 복잡도, 문제 풀이 패턴, 오답 및 반례 |
| [System Programming](notes/system-programming/) | C/C++, POSIX, 프로세스, 스레드, IPC, 동기화, 소켓 |
| [Undergraduate Courses](notes/undergraduate/) | 운영체제, 컴퓨터구조, 네트워크, 데이터베이스, 디지털 회로 |
| [Linux Kernel](notes/linux-kernel/) | 스케줄링, 가상 메모리, 커널 분석, 드라이버, tracing |
| [Storage & File Systems](notes/storage/) | VFS, ext4/F2FS, SSD·Flash, NVMe, I/O 경로 |
| [Graduate Study](notes/graduate/) | KAIST 수업, 논문 읽기, 재현 실험, 연구 준비 |

글은 [`notes/`](notes/)에, 실제 코드·테스트·실험은 [`labs/`](labs/)에 보관한다. 실습 코드는 실행 방법과 결과를 함께 기록하는 것을 원칙으로 한다.

## 새 노트 작성

1. 공부 분야에 해당하는 `notes/` 하위 폴더를 선택한다.
2. [일반 노트 템플릿](notes/_templates/note.mdx), [알고리즘 풀이 템플릿](notes/_templates/algorithm.mdx), [실험 기록 템플릿](notes/_templates/experiment.mdx) 중 하나를 복사한다.
3. 본문을 **한국어**로 작성하고, 직접 실행·검증한 내용과 참고한 내용은 구분한다.
4. 작성 중에는 `draft: true`, `reviewed: false`로 둔다.
5. 검토 후 `draft: false`, `reviewed: true`, `sensitivity: public`으로 변경하면 [개인 사이트의 Notes](https://petooooo.github.io/notes/)에 자동 반영된다.

자세한 작성 및 공개 기준은 [docs/WRITING.md](docs/WRITING.md), 앞으로의 공부 방향은 [학습 로드맵](notes/study-roadmap.mdx)을 참고한다.

> **주의:** 이 저장소는 공개 저장소다. `draft: true`는 **개인 사이트에만 보이지 않게** 하는 설정이며, GitHub에서는 초안도 볼 수 있다. 군 내부 운영 정보, 연구실 비공개 자료, 과목별 저작권 자료, API 키, 계정 정보 등은 여기에 올리지 않는다.

## 개인 사이트와 연동

원본은 이 저장소에서 관리한다. 사이트는 GitHub Actions 빌드 시 공개·검토 완료된 Markdown/MDX 파일을 가져온다. 자동 확인은 약 1시간 간격이며 GitHub Actions 스케줄에 따라 지연될 수 있다. 즉시 게시하려면 웹사이트 저장소의 `Deploy GitHub Pages` 워크플로를 수동 실행하면 된다.

**일반 공부 노트는 앞으로 여기서 작성**하고, 사이트 레이아웃·메뉴·CV·프로필 수정이 필요할 때만 웹사이트 저장소를 변경한다. 과거에 웹사이트 저장소에 작성된 Notes는 현재 별도로 보존되어 있다.
