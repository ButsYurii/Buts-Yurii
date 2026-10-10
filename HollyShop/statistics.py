from catalog import products


def get_statistics():
    """Обчислює статистику товарів у магазині."""
    total_products = len(products)
    total_stock = sum(
        product["stock"] for product in products.values()
    )
    total_value = sum(
        product["price"] * product["stock"]
        for product in products.values()
    )

    return {
        "total_products": total_products,
        "total_stock": total_stock,
        "total_value": total_value,
    }