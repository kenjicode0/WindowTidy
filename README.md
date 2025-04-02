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

## Usage (early CLI)
- Compute a grid cell rectangle for a given screen size:

```
windowtidy 3 2 1 0 1440 900 0 0
# -> prints x,y,w,h for cell (1,0) in a 3x2 grid
```

This is a placeholder until the accessibility layer is added.

## Dev
- Language: Python 3.11+
- Platform target: macOS first; layout math is platform‑agnostic
- No build required; small CLI for now

## License
MIT
