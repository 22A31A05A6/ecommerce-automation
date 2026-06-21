import pytest
from tests.pages import LoginPage, InventoryPage


@pytest.fixture(autouse=True)
def login(page):
    """Log in before every test in this module."""
    lp = LoginPage(page)
    lp.open()
    lp.login("standard_user", "secret_sauce")


class TestInventory:

    def test_products_are_displayed(self, page):
        """Inventory page should show 6 products."""
        inv = InventoryPage(page)
        products = inv.get_all_product_names()
        assert len(products) == 6, f"Expected 6 products, got {len(products)}"

    def test_add_single_item_updates_cart_badge(self, page):
        """Adding one item should show badge count of 1."""
        inv = InventoryPage(page)
        inv.add_first_product_to_cart()
        assert inv.get_cart_count() == 1

    def test_sort_price_low_to_high(self, page):
        """Products sorted low-to-high should be in ascending price order."""
        inv = InventoryPage(page)
        inv.sort_products("lohi")
        prices = inv.get_all_prices()
        assert prices == sorted(prices), "Prices are not in ascending order"

    def test_sort_price_high_to_low(self, page):
        """Products sorted high-to-low should be in descending price order."""
        inv = InventoryPage(page)
        inv.sort_products("hilo")
        prices = inv.get_all_prices()
        assert prices == sorted(prices, reverse=True), "Prices are not in descending order"

    def test_sort_name_a_to_z(self, page):
        """Products sorted A-Z should be in alphabetical order."""
        inv = InventoryPage(page)
        inv.sort_products("az")
        names = inv.get_all_product_names()
        assert names == sorted(names)

    def test_add_multiple_items_updates_cart_count(self, page):
        """Adding 3 items should update badge to 3."""
        inv = InventoryPage(page)
        for _ in range(3):
            inv.page.locator("[data-test^='add-to-cart']").nth(_).click()
        assert inv.get_cart_count() == 3
