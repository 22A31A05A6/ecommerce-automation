import pytest
from playwright.sync_api import sync_playwright

# ── Browsers to test against ──────────────────────────────────────────────────
BROWSERS = ["chromium", "firefox", "webkit"]


def pytest_addoption(parser):
    parser.addoption(
        "--browser-name",
        action="store",
        default="chromium",
        choices=BROWSERS,
        help="Browser to run tests on",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=True,
        help="Run in headless mode",
    )


@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("--browser-name")


@pytest.fixture(scope="session")
def headless(request):
    return request.config.getoption("--headless")


@pytest.fixture(scope="function")
def page(browser_name, headless):
    """Yield a fresh Playwright page for each test, then close it."""
    with sync_playwright() as p:
        browser_type = getattr(p, browser_name)
        browser = browser_type.launch(headless=headless)
        context = browser.new_context(
            viewport={"width": 1280, "height": 720},
            record_video_dir="reports/videos/",
        )
        page = context.new_page()
        yield page
        context.close()
        browser.close()
