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



## Suite Design: Smoke and Regression tests (for CI)

We can use pytest markers to split tests to smoke and regression tests 

- Smoke: quick, core flows; run on every push/PR.
- Regression: full coverage; run nightly or after merge to main.

How to use:
1. Define markers in pytest.ini (see below).
2. Mark tests:
   - `@pytest.mark.smoke`
   - `@pytest.mark.regression`
3. Run locally (Windows PowerShell):
   - `python -m pytest -m smoke -q`
   - `python -m pytest -m "regression or not smoke" -q`

## Remove flaky tests:   

1. Use stable selectors(data-testid, data-cy, data-test). Avoid brittle selectors such as texts.
2. Use in-built methods such as wait for load, wait for response, mainly during navigations.
3. Keep the tests clear and readable.
4. Use explicit timeouts if required.
5. Use proper global timeout for tests.
6. Use moke/stub for slow and external api's.
7. Use tool specific feature to debug the slow and flaky tests(Trace viewer, logs and history, new  flaky/slow tests separation in latest playwright report).
8. Skip the tests until flakyness is fixed.
9. Use retries to avoid infra/network issues during test.
10. Have proper teardown/cleanup code.


## Scaling: Refactorings for dozens of flows

Apply these features to keep the suite maintainable:

1. Shared fixtures and helpers
- Use fixtures in `conftest.py` for reusable code.
- Example: logins, authentication for tests.

2. Base page class
- Create a `BasePage` class with common methods (`click`, `fill`, `wait_for_selector`, `navigate`).
- All page objects inherit from `BasePage`.

3. Test data management
- Move test data (usernames, products, form inputs) to separate files (JSON, Python constants).
- Use `@pytest.mark.parametrize` for data-driven tests.

4. Organize tests by feature/module
- Split tests into folders: `tests/login/`, `tests/checkout/`, `tests/cart/`.
- Use separate conftest.py per folder for module-specific fixtures.

5. Custom assertions and wait helpers
- Create utility functions for common assertions (`assert_page_title`, `assert_element_visible`).
- Add wait helpers (`wait_for_navigation_complete`, `wait_for_api_response`).

6. Page component pattern usage
- Extract reusable UI components (header, footer, modals) into component classes.

7. Parallel executions
- Use `pytest-xdist` to run tests in parallel: `pytest -n auto`.
- Ensure tests are isolated (no shared state, unique test data).

8. Tagging and grouping
- Use multiple markers for different type of test cases

9. Reporting
- Integrate with test management tools (Allure, Xray).
- Add logging for debugging