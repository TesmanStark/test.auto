
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_valid_login(page):

    # Login
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")

    # Verify inventory page
    inventory = InventoryPage(page)
    expect(inventory.title).to_have_text("Products")


def test_add_to_cart(page):

    # Login
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")

    # Add product to cart
    inventory = InventoryPage(page)
    inventory.add_backpack()
    expect(inventory.cart_badge).to_have_text("1")

    # Open cart
    inventory.open_cart()

    # Verify cart
    expect(page.locator(".cart_item")).to_have_count(1)

def test_invalid_login(page):

    login = LoginPage(page)
    login.navigate()

    login.login("invalid_user", "wrong_password")

    expect(login.error_message).to_be_visible()
    expect(login.error_message).to_contain_text(
        "Username and password do not match"
    )

def test_locked_out_user(page):

    login = LoginPage(page)
    login.navigate()

    login.login("locked_out_user", "secret_sauce")

    expect(login.error_message).to_be_visible()
    expect(login.error_message).to_contain_text(
        "Sorry, this user has been locked out"
    )
