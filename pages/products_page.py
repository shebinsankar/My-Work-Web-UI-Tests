from .base_page import BasePage
from typing import List


class ProductsPage(BasePage):
    SORT_SELECT = '.product_sort_container'
    ITEM = '.inventory_item'

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
            f".inventory_item:has-text(\"{name}\") button:has-text('Add to cart')")
        locator.first.click()

    def go_to_cart(self):
        self.click('#shopping_cart_container a')
