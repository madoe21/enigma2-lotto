# Codebase map (onboarding 2026-07-08)

**enigma2-lotto** — Enigma2 (OpenATV 7.6) plugin: German lottery (Lotto 6aus49
etc.) results on the TV. Python. ~800 LOC.

## Layout
- `src/LottoDE/plugin.py` (~104 LOC) — entry.
- `src/LottoDE/core/lotto_service.py` (~191) — results fetch + parsing.
  **`core/` is confirmed free of enigma2 imports** (platform-agnostic).
- `src/LottoDE/screens.py` (~317) — enigma2 GUI.
- `res/`, `control/`, `build/` (gitignored ipk).

## Conventions
- Enigma2 Py3; timeouts on the results fetch.

## Kodi portability: **already split (reference shape)**
Clean `core/` (data, enigma2-free) vs `screens.py`/`plugin.py` (enigma2 GUI).
This is the **target pattern** the monolithic plugins (fritzcall, fritzhome,
fritzmon, homematic, openliga-db, spritpreise-checker, wireguard) should be
refactored toward. A Kodi port only needs a `platform/kodi/` GUI on top of the
existing `core/`.
