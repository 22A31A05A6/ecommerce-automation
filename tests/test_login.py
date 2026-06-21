import pytest
from tests.pages import LoginPage, InventoryPage
from tests.test_data import INVALID_CREDENTIALS


class TestLogin:

    def test_successful_login(self, page):
        """Standard user should land on inventory page after login."""
        login = LoginPage(page)
        login.open()
        login.login("standard_user", "secret_sauce")
        assert "inventory" in page.url, "Expected redirect to inventory page"

    @pytest.mark.parametrize(
        "username,password,expected_error", INVALID_CREDENTIALS
    )
    def test_invalid_login_shows_error(self, page, username, password, expected_error):
        """Invalid credentials should show appropriate error messages."""
        login = LoginPage(page)
        login.open()
        login.login(username, password)
        assert login.is_error_visible(), "Error message not displayed"
        assert expected_error in login.get_error_message()

    def test_locked_out_user_cannot_login(self, page):
        """Locked-out user should see a specific error."""
        login = LoginPage(page)
        login.open()
        login.login("locked_out_user", "secret_sauce")
        assert "locked out" in login.get_error_message().lower()

    def test_page_title(self, page):
        """Login page should have correct title."""
        login = LoginPage(page)
        login.open()
        assert "Swag Labs" in login.get_title()
