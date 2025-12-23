from .base_page import BasePage
from typing import List


class CheckoutPage(BasePage):
    def fill_info(self, first: str, last: str, postal: str):
        self.fill('#first-name', first)
        self.fill('#last-name', last)
        self.fill('#postal-code', postal)
        self.click('#continue')

    def overview_items(self) -> List[dict]:
        items = []
        for item in self.page.locator('.cart_item').all():
            name = item.locator('.inventory_item_name').inner_text()
            price = float(item.locator(
                '.inventory_item_price').inner_text().replace('$', ''))
            items.append({'name': name, 'price': price})
        return items

    def item_total(self) -> float:
        text = self.text('#checkout_summary_container .summary_subtotal_label')
        # expected format: "Item total: $xx.xx"
        return float(text.split('$')[-1])

    def finish(self):
        self.click('#finish')
