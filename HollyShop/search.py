from catalog import products


def search_products(query):
    """Шукає товари за назвою."""
    results = []

    for product_id, product in products.items():
        if query.lower() in product["name"].lower():
            results.append({
                "id": product_id,
                "name": product["name"],
                "price": product["price"],
                "stock": product["stock"],
            })

    return results