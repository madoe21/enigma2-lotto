# Lotto DE – Enigma2 Plugin

[![Built with aiflow](https://img.shields.io/badge/built%20with-aiflow-6b46c1)](https://github.com/cyber93de/aiflow)

📖 [Project page & install instructions](https://madoe21.github.io/enigma2-lotto/)

Enigma2 plugin that displays the lottery numbers of the **current week**:

- **Eurojackpot**: Tuesday and Friday
- **LOTTO 6aus49**: Wednesday and Saturday

Navigation:

- **Left**: one week back
- **Right**: one week forward (up to the current week)

Numbers are displayed in white ball-style fields with black text.

---

## Data source

The plugin uses the JSON endpoints of Lotto Brandenburg:

- `/app/getDrawResultYears`
- `/app/getDrawResultDates`
- `/app/getDrawResults`

For Eurojackpot `gameType=EURO` is used, for 6aus49 `gameType=LOTTO`.

---

## Architecture

The structure is designed for easy Kodi migration:

- `src/LottoDE/core/api_client.py`: HTTP/JSON access
- `src/LottoDE/core/lotto_service.py`: week and game logic
- `src/LottoDE/core/models.py`: data objects
- `src/LottoDE/core/week_logic.py`: date/ISO week logic
- `src/LottoDE/screens.py`: Enigma2 UI layer
- `src/LottoDE/plugin.py`: plugin entry and wiring

The business logic is separated from the Enigma2 presentation layer.

---

## Build & deploy

Prerequisites:

- Linux/WSL with `make`, `tar`, `ar`
- Optional: `dos2unix`

Configure `.env`:

```env
BOX_HOST=192.168.1.10
BOX_USER=root
BOX_PORT=22
```

Commands:

```bash
make ipk
make deploy
make clean
```

---

## Notes

- Data may appear with a delay depending on the upstream provider.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Found a bug or have a suggestion for improvement? Please create an issue or pull request.

I appreciate everyone who supports me and the project! For any requests and suggestions, feel free to provide feedback.

<p>
  <a href="https://www.buymeacoffee.com/madoe21">
    <img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" height="50" alt="Buy Me a Coffee">
  </a>

  <a href="https://ko-fi.com/madoe21">
    <img src="https://storage.ko-fi.com/cdn/kofi3.png?v=3" height="50" alt="Ko-fi">
  </a>

  <a href="https://paypal.me/MartinD809">
    <img src="https://www.paypalobjects.com/webstatic/mktg/logo/pp_cc_mark_111x69.jpg" height="50" alt="PayPal">
  </a>
</p>

---

## Built with aiflow

This project was built with support from **[aiflow](https://cyber93de.github.io/aiflow/)** — *built with aiflow*.
