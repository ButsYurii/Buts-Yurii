from catalog import products


def sort_products(reverse=False):
    """Сортує товари за ціною."""
    sorted_products = sorted(
        products.items(),
        key=lambda item: item[1]["price"],
        reverse=reverse,
    )

    return sorted_products