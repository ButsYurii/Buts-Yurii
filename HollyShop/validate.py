def validate_product(name, price, stock):
    """Перевіряє коректність даних товару."""
    if not isinstance(name, str) or not name.strip():
        return False

    if isinstance(price, bool) or not isinstance(price, (int, float)):
        return False

    if isinstance(stock, bool) or not isinstance(stock, int):
        return False

    if price <= 0 or stock <= 0:
        return False

    return True