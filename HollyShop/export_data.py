import json
import os

from catalog import products


def export_products(filename="products.json"):
    """Зберігає каталог товарів у JSON-файл."""
    file_path = os.path.abspath(filename)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(
            products,
            file,
            ensure_ascii=False,
            indent=4
        )

    return file_path