import faulthandler

from catalog import products


def add_product(name, price, stock):
    """Додає новий товар до каталогу."""
    if not name.strip():
        return False

    if price < 0 or stock <0:
        return False

    product_id = max(products.keys(), default=0) + 1

    products[product_id] = {
        "name": name.strip(),
        "price": float(price),
        "stock": int(stock),
    }

    return True