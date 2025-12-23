import os
import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        help="Run browser headed (default: headed)",
    )
    parser.addoption(
        "--record-video",
        action="store_true",
        help="Record video for each test (overrides RECORD_VIDEO env)",
    )
    parser.addoption(
        "--slow-mo",
        type=int,
        default=None,
        help="Slow down Playwright operations by ms (overrides SLOW_MO_MS)",
    )
    parser.addoption(
        "--browser",
        type=str,
        default=None,
        help="Browser channel to use (chrome, msedge, etc.)",
    )


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as pw:
        yield pw


@pytest.fixture(scope="session")
def browser(playwright_instance, request):
    config = request.config
    # headed flag overrides env var; default is headed (headless=False)
    if config.getoption("headed"):
        headless = False
    else:
        headless = os.getenv('HEADLESS', 'false').lower() in (
            '1', 'true', 'yes')

    slow_opt = config.getoption("slow_mo")
    if slow_opt is not None:
        slow_ms = int(slow_opt)
    else:
        slow_ms = int(os.getenv('SLOW_MO_MS', '200'))

    browser_channel = config.getoption(
        "browser") or os.getenv('BROWSER_CHANNEL', 'chrome')

    browser = playwright_instance.chromium.launch(
        channel=browser_channel, headless=headless, slow_mo=slow_ms
    )
    yield browser
    browser.close()


@pytest.fixture
def page(browser, request):
    # video recording option removed from fixture; keep default viewport
    ctx_kwargs = {"viewport": {"width": 1280, "height": 720}}

    context = browser.new_context(**ctx_kwargs)
    page = context.new_page()
    yield page

    # try to take a final screenshot (best-effort)
    try:
        screenshot_path = f"videos/{request.node.name}_final_screenshot.png"
        page.screenshot(path=screenshot_path)
    except Exception:
        pass

    context.close()
