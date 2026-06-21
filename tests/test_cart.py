import pytest
from tests.pages import LoginPage, InventoryPage, CartPage


@pytest.fixture(autouse=True)
def login_and_add_item(page):
    """Log in and add one item to cart before each test."""
    lp = LoginPage(page)
    lp.open()
    lp.login("standard_user", "secret_sauce")
    inv = InventoryPage(page)
    inv.add_first_product_to_cart()
    inv.go_to_cart()


class TestCart:

    def test_cart_has_correct_item_count(self, page):
        cart = CartPage(page)
        assert cart.get_item_count() == 1

    def test_cart_shows_correct_item_name(self, page):
        """Item added from inventory should appear in cart."""
        cart = CartPage(page)
        names = cart.get_item_names()
        assert len(names) == 1
        assert names[0] != ""

    def test_remove_item_empties_cart(self, page):
        """Removing the only item should leave cart empty."""
        cart = CartPage(page)
        cart.remove_first_item()
        assert cart.get_item_count() == 0

    def test_continue_shopping_returns_to_inventory(self, page):
        """Continue Shopping should navigate back to inventory."""
        cart = CartPage(page)
        cart.continue_shopping()
        assert "inventory" in page.url

    def test_cart_item_has_positive_price(self, page):
        cart = CartPage(page)
        prices = cart.get_item_prices()
        assert all(p > 0 for p in prices), "All item prices should be > 0"
