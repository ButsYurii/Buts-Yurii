from catalog import products


def remove_product(product_id):
    """Видаляє товар із каталогу."""
    if product_id not in products:
        return False

    del products[product_id]

    return True