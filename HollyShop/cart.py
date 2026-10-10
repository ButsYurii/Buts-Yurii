from catalog import products


def add_to_cart(cart, product_id, quantity=1):
    """Додає товар до кошика"""
    if product_id not in products:
        return cart

    if quantity <= 0:
        return cart

    if products[product_id]["stock"] < quantity:
        return cart

    cart[product_id] = cart.get(product_id, 0) + quantity

    return cart