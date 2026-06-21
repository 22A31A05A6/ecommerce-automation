from .base_page import BasePage


class CartPage(BasePage):
    # ── Locators ──────────────────────────────────────────────────────────────
    CART_ITEMS         = ".cart_item"
    ITEM_NAME          = ".inventory_item_name"
    ITEM_PRICE         = ".inventory_item_price"
    REMOVE_BTN         = "[data-test^='remove']"
    CHECKOUT_BTN       = "[data-test='checkout']"
    CONTINUE_SHOPPING  = "[data-test='continue-shopping']"

    URL = "https://www.saucedemo.com/cart.html"

    def get_cart_items(self) -> list:
        return self.page.locator(self.CART_ITEMS).all()

    def get_item_count(self) -> int:
        return self.page.locator(self.CART_ITEMS).count()

    def get_item_names(self) -> list:
        return self.page.locator(self.ITEM_NAME).all_inner_texts()

    def get_item_prices(self) -> list:
        raw = self.page.locator(self.ITEM_PRICE).all_inner_texts()
        return [float(p.replace("$", "")) for p in raw]

    def remove_first_item(self):
        self.page.locator(self.REMOVE_BTN).first.click()

    def proceed_to_checkout(self):
        self.page.click(self.CHECKOUT_BTN)

    def continue_shopping(self):
        self.page.click(self.CONTINUE_SHOPPING)
