class BasePage:
    """All page objects inherit from here."""

    def __init__(self, page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()

    def wait_for_url(self, url_pattern: str):
        self.page.wait_for_url(url_pattern)

    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).inner_text()

    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()
