import json
import os
from fileinput import filename

from pygments.lexers import data


def import_products(filename="products.json"):
    """Завантажує каталог товарів із JSON-файлу."""
    file_path = os.path.abspath(filename)

    if not os.path.exists(file_path):
        return None

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError):
        return None

    if not isinstance(data, dict):
        return None

    return data