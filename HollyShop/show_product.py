from rich import console

from catalog import products
from rich.console import Console
from rich.panel import Panel


console = Console()


def show_product(product_id):
    """Виводить детальну інформацію про товар."""
    product = products.get(product_id)

    if product is None:
        console.print("Товар не знайдено.", style="bold red")
        return False

    details = (
        f"Назва: {product['name']}\n"
        f"Ціна: {product['price']:.2f} грн\n"
        f"Кількість на складі: {product['stock']}"
    )

    console.print(
        Panel(
            details,
            title=f"Товар №{product_id}",
            border_style="green",
        )
    )

    return True