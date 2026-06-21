import pytest


# ── Valid users on saucedemo.com ──────────────────────────────────────────────
VALID_USERS = [
    ("standard_user",        "secret_sauce"),
    ("problem_user",         "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
]

INVALID_CREDENTIALS = [
    ("",               "secret_sauce",   "Username is required"),
    ("standard_user",  "",               "Password is required"),
    ("wrong_user",     "wrong_pass",     "Username and password do not match"),
    ("locked_out_user","secret_sauce",   "Sorry, this user has been locked out"),
]

CUSTOMER_INFO = {
    "valid":   {"first": "Samuel", "last": "Guttula", "postal": "533308"},
    "no_first":{"first": "",       "last": "Guttula", "postal": "533308"},
    "no_last": {"first": "Samuel", "last": "",         "postal": "533308"},
    "no_zip":  {"first": "Samuel", "last": "Guttula",  "postal": ""},
}


@pytest.fixture(params=VALID_USERS, ids=[u[0] for u in VALID_USERS])
def valid_user(request):
    username, password = request.param
    return {"username": username, "password": password}


@pytest.fixture(
    params=INVALID_CREDENTIALS,
    ids=[f"{u[0] or 'empty'}-{u[1] or 'empty'}" for u in INVALID_CREDENTIALS],
)
def invalid_credentials(request):
    username, password, expected_error = request.param
    return {"username": username, "password": password, "error": expected_error}
