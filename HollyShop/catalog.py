from tabulate import  tabulate


products = {
    1: {"name": "Мишка", "price": 2199, "stock":99},
    2: {"name": "Клавіатура", "price": 3877, "stock":99},
    3: {"name": "Монітор", "price": 8799, "stock":99},
    4: {"name": "Системний блок", "price": 14988, "stock":99},
}


def show_catalog():
    table = []

    for product_id, product in products.items():
        table.append([
            product_id,
            product["name"],
            f'{product["price"]:.2f} грн',
            product["stock"]
        ])

    print(
        tabulate(
            table,
            headers=["ID", "Назва", "Ціна", "Кількість"],
            tablefmt="grid",
        )
    )