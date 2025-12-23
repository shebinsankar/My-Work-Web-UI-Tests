UI automation for https://www.saucedemo.com/ using Playwright + Python (POM)

Quick start


```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```


```bash
pip install -r requirements.txt
python -m playwright install
```


Running tests

The test suite uses a `page` fixture in `conftest.py` which launches a Chromium-based browser by channel (default: Chrome).

Environment variables (optional):
- `SLOW_MO_MS`: slow Playwright actions by N ms (default `200`).
- `HEADLESS`: `true`/`false` to run headless (default `false`).
- `BROWSER_CHANNEL`: browser channel name (default `chrome`).

Pytest CLI options (override env vars):
- `--headed` : run headed (equivalent to `HEADLESS=false`).
- `--slow-mo=N` : slow down actions by N milliseconds.
- `--browser=name` : browser channel to use (e.g. `chrome`, `msedge`).

Examples

Run headed Chrome with 300ms slow-down and html report:

```powershell
python -m pytest -q --headed --slow-mo=300 --browser=chrome --html=reports/report.html --self-contained-html
```

Or set environment variables:

```powershell
# $env:SLOW_MO_MS='300'
# $env:RECORD_VIDEO='true'
python -m pytest -q
```

Artifacts

- **Screenshots / Screenshots:** Saved in the `videos/` directory as PNG files by default (the fixture saves a final screenshot per test).
- **HTML report:** A self-contained HTML report is generated at `reports/report.html` by default when `pytest-html` is enabled.

- Files of interest

- [pages/login_page.py](pages/login_page.py)
- [pages/products_page.py](pages/products_page.py)
- [pages/cart_page.py](pages/cart_page.py)
- [pages/checkout_page.py](pages/checkout_page.py)
- [tests/test_saucedemo_flow.py](tests/test_saucedemo_flow.py)
