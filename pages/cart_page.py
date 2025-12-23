from .base_page import BasePage


class CartPage(BasePage):
    ITEM = '.cart_item'

    def get_cart_items(self):
        items = []
        for item in self.page.locator(self.ITEM).all():
            name = item.locator('.inventory_item_name').inner_text()
            price = float(item.locator(
                '.inventory_item_price').inner_text().replace('$', ''))
            items.append({'name': name, 'price': price})
        return items

    def checkout(self):
        self.click('#checkout')
