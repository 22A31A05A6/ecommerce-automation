from .base_page import BasePage


class CheckoutPage(BasePage):
    # ── Step 1 locators ───────────────────────────────────────────────────────
    FIRST_NAME    = "[data-test='firstName']"
    LAST_NAME     = "[data-test='lastName']"
    POSTAL_CODE   = "[data-test='postalCode']"
    CONTINUE_BTN  = "[data-test='continue']"
    ERROR_MESSAGE = "[data-test='error']"

    # ── Step 2 locators ───────────────────────────────────────────────────────
    SUMMARY_SUBTOTAL = ".summary_subtotal_label"
    SUMMARY_TAX      = ".summary_tax_label"
    SUMMARY_TOTAL    = ".summary_total_label"
    FINISH_BTN       = "[data-test='finish']"

    # ── Confirmation locators ─────────────────────────────────────────────────
    CONFIRM_HEADER   = ".complete-header"
    CONFIRM_TEXT     = ".complete-text"

    def fill_customer_info(self, first: str, last: str, postal: str):
        self.page.fill(self.FIRST_NAME, first)
        self.page.fill(self.LAST_NAME, last)
        self.page.fill(self.POSTAL_CODE, postal)

    def continue_checkout(self):
        self.page.click(self.CONTINUE_BTN)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def get_total(self) -> str:
        return self.get_text(self.SUMMARY_TOTAL)

    def finish_order(self):
        self.page.click(self.FINISH_BTN)

    def get_confirmation_header(self) -> str:
        return self.get_text(self.CONFIRM_HEADER)
