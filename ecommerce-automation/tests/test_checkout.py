import pytest
from tests.pages import LoginPage, InventoryPage, CartPage, CheckoutPage
from tests.test_data import CUSTOMER_INFO


@pytest.fixture(autouse=True)
def reach_checkout(page):
    """Log in → add item → cart → checkout step 1."""
    LoginPage(page).open()
    LoginPage(page).login("standard_user", "secret_sauce")
    inv = InventoryPage(page)
    inv.add_first_product_to_cart()
    inv.go_to_cart()
    CartPage(page).proceed_to_checkout()


class TestCheckout:

    def test_successful_checkout_end_to_end(self, page):
        """Full happy-path: fill info → overview → finish → confirmation."""
        co = CheckoutPage(page)
        info = CUSTOMER_INFO["valid"]
        co.fill_customer_info(info["first"], info["last"], info["postal"])
        co.continue_checkout()
        assert "checkout-step-two" in page.url
        total = co.get_total()
        assert "Total:" in total
        co.finish_order()
        assert "Thank you" in co.get_confirmation_header()

    def test_checkout_requires_first_name(self, page):
        co = CheckoutPage(page)
        info = CUSTOMER_INFO["no_first"]
        co.fill_customer_info(info["first"], info["last"], info["postal"])
        co.continue_checkout()
        assert "First Name is required" in co.get_error_message()

    def test_checkout_requires_last_name(self, page):
        co = CheckoutPage(page)
        info = CUSTOMER_INFO["no_last"]
        co.fill_customer_info(info["first"], info["last"], info["postal"])
        co.continue_checkout()
        assert "Last Name is required" in co.get_error_message()

    def test_checkout_requires_postal_code(self, page):
        co = CheckoutPage(page)
        info = CUSTOMER_INFO["no_zip"]
        co.fill_customer_info(info["first"], info["last"], info["postal"])
        co.continue_checkout()
        assert "Postal Code is required" in co.get_error_message()

    def test_order_total_is_positive(self, page):
        co = CheckoutPage(page)
        info = CUSTOMER_INFO["valid"]
        co.fill_customer_info(info["first"], info["last"], info["postal"])
        co.continue_checkout()
        total_text = co.get_total()
        total_value = float(total_text.replace("Total: $", ""))
        assert total_value > 0
