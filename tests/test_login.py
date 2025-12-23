from pages import LoginPage


def test_login_success(page):
    login = LoginPage(page)
    login.launch()
    login.login('standard_user', 'secret_sauce')

    # Verify we land on the products/inventory page by checking title and product items
    assert page.locator('.title').inner_text() == 'Products'
    assert page.locator('.inventory_item').count() > 0
