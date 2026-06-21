# E-Commerce Test Automation Framework

End-to-end test automation framework for [SauceDemo](https://www.saucedemo.com/) built with **Playwright + PyTest** using the **Page Object Model** design pattern.

## 🧪 What's Tested

| Module | Scenarios |
|--------|-----------|
| Login | Valid login, invalid credentials, locked user, empty fields |
| Inventory | Product count, add to cart, sort by price/name |
| Cart | Item count, remove item, continue shopping |
| Checkout | Full happy path, missing field validations, total price |

## 🛠️ Tech Stack

- **Playwright** — cross-browser automation (Chromium, Firefox, WebKit)
- **PyTest** — test runner with parameterized fixtures
- **Page Object Model** — clean separation of locators and test logic
- **pytest-html** — HTML test reports

## 📁 Project Structure

```
ecommerce-automation/
├── conftest.py               # Browser fixture setup
├── pytest.ini                # PyTest config
├── requirements.txt
├── tests/
│   ├── pages/
│   │   ├── base_page.py      # Shared page methods
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   ├── test_data.py          # Parameterized test inputs
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
└── reports/                  # HTML reports generated here
```

## 🚀 Setup & Run

```bash
# Install dependencies
pip install -r requirements.txt
playwright install

# Run all tests (Chromium, headless)
pytest

# Run on Firefox
pytest --browser-name=firefox

# Run on all browsers
pytest --browser-name=chromium
pytest --browser-name=firefox
pytest --browser-name=webkit

# Run headed (visible browser)
pytest --no-header --headed
```

HTML report is saved to `reports/report.html` after each run.
