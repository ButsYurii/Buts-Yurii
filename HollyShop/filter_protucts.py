from catalog import products


def filter_products(min_price=0, max_price=float("inf")):
    """Фільтрує товари за діапазоном цін."""
    filtered_products = []

    for product_id, product in products.items():
        price = product["price"]

        if min_price <= price <= max_price:
            filtered_products.append((product_id, product))

        return filtered_products