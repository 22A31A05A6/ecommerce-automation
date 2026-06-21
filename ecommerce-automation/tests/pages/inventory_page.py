from .base_page import BasePage


class InventoryPage(BasePage):
    # ── Locators ──────────────────────────────────────────────────────────────
    PRODUCT_TITLE      = ".inventory_item_name"
    ADD_TO_CART_BTN    = "[data-test^='add-to-cart']"
    CART_BADGE         = ".shopping_cart_badge"
    CART_ICON          = ".shopping_cart_link"
    SORT_DROPDOWN      = "[data-test='product-sort-container']"
    PRODUCT_PRICES     = ".inventory_item_price"

    URL = "https://www.saucedemo.com/inventory.html"

    def get_all_product_names(self) -> list:
        return self.page.locator(self.PRODUCT_TITLE).all_inner_texts()

    def add_first_product_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BTN).first.click()

    def add_product_by_name(self, name: str):
        # Convert product name to data-test id format
        slug = name.lower().replace(" ", "-").replace("(", "").replace(")", "")
        self.page.click(f"[data-test='add-to-cart-{slug}']")

    def get_cart_count(self) -> int:
        badge = self.page.locator(self.CART_BADGE)
        if badge.is_visible():
            return int(badge.inner_text())
        return 0

    def go_to_cart(self):
        self.page.click(self.CART_ICON)

    def sort_products(self, option: str):
        """option: 'az', 'za', 'lohi', 'hilo'"""
        self.page.select_option(self.SORT_DROPDOWN, option)

    def get_all_prices(self) -> list:
        raw = self.page.locator(self.PRODUCT_PRICES).all_inner_texts()
        return [float(p.replace("$", "")) for p in raw]
