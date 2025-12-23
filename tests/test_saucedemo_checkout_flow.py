from pages import LoginPage, ProductsPage, CartPage, CheckoutPage


def test_saucedemo_checkout_flow(page):

    login = LoginPage(page)
    login.launch()
    login.login('standard_user', 'secret_sauce')

    products = ProductsPage(page)
    # Sort the products by 'price low->high'
    products.sort_by('Price (low to high)')

    list_before = products.list_items()
    assert len(list_before) > 0

    # add first two items to cart
    to_add = [list_before[0]['name']]
    if len(list_before) > 1:
        to_add.append(list_before[1]['name'])

    for name in to_add:
        products.add_to_cart_by_name(name)

    products.go_to_cart()

    cart = CartPage(page)
    cart_items = cart.get_cart_items()
    cart_names = [c['name'] for c in cart_items]
    for name in to_add:
        assert name in cart_names

    # proceed to checkout
    cart.checkout()

    checkout = CheckoutPage(page)
    checkout.fill_info('Test', 'User', '12345')

    overview = checkout.overview_items()
    overview_names = [i['name'] for i in overview]
    for name in to_add:
        assert name in overview_names

    # assert item total equals sum of item prices
    expected_total = sum(i['price'] for i in overview)
    displayed_total = checkout.item_total()
    assert abs(expected_total - displayed_total) < 0.01
