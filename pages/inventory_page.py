
from playwright.sync_api import Page


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.title = page.locator(".title")
        self.backpack = page.locator("#add-to-cart-sauce-labs-backpack")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    # Actions
    def add_backpack(self):
        self.backpack.click()

    def open_cart(self):
        self.cart_icon.click()
