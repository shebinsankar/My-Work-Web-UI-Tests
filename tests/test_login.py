import pytest
from pages import LoginPage, ProductsPage


@pytest.mark.smoke
def test_login_success(page):
    login = LoginPage(page)
    login.launch()
    login.login('standard_user', 'secret_sauce')

    # Verify we land on the products/inventory page by checking title and product items
    products = ProductsPage(page)
    assert products.getTitle() == 'Products'
    assert page.locator(products.ITEM).count() > 0
