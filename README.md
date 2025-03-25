# WindowTidy

WindowTidy is a tiny, single‑purpose macOS window layout helper written as a solo weekend project. It lets you quickly snap windows to sensible positions using simple keyboard shortcuts and a small tray icon. The goal is a fast, dependency‑light tool you can tweak without wading through heavy settings.

This repo evolves incrementally with small, realistic commits, like a real personal project: a little bit each evening.

## Status
- Early scaffolding; CLI stub and layout core planned
- Focus: clean code, minimal dependencies, clear docs

## Roadmap
- Core grid model and layout math
- Cross‑app window inspector (accessibility API)
- Hotkey handler and preset actions
- Config file with profiles
- Basic test coverage for layout math

## Dev
- Language: Python 3.11+
- Platform target: macOS first; layout math is platform‑agnostic
- No build required; small CLI for now

## License
MIT

