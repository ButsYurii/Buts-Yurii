from catalog import products


def calculate_total(cart):
    """Обчислює загальну вартість товарів у кошику."""
    total = 0.0

    for product_id, quantity in cart.items():
        price = products[product_id]["price"]
        total += price * quantity

    return round(total, 2)