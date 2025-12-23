from .base_page import BasePage
from typing import List


class ProductsPage(BasePage):
    TITLE = "[data-test='title']"
    SORT_SELECT = "[data-test='product-sort-container']"
    ITEM = "[data-test = 'inventory-item-description']"

    def getTitle(self) -> str:
        return self.page.locator(self.TITLE).inner_text()

    def sort_by(self, value: str):
        # value examples: "Price (low to high)", "Name (Z to A)"
        self.page.locator(self.SORT_SELECT).select_option(label=value)

    def list_items(self) -> List[dict]:
        items = []
        for item in self.page.locator(self.ITEM).all():
            name = item.locator('.inventory_item_name').inner_text()
            price_text = item.locator('.inventory_item_price').inner_text()
            price = float(price_text.replace('$', ''))
            items.append({'name': name, 'price': price, 'element': item})
        return items

    def add_to_cart_by_name(self, name: str):
        locator = self.page.locator(
            f".inventory_item:has-text(\"{name}\") button[data-test^=\"add-to-cart\"]")
        locator.first.click()

    def go_to_cart(self):
        self.click("[data-test='shopping-cart-link']")
