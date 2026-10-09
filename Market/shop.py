from os import name

products = {
    1: {"name": "Мишка", "price": 120.11, "stock": 99},
    2: {"name": "Клавіатура", "price": 210, "stock": 99},
    3: {"name": "Монітор", "price": 440, "stock": 99},
    4: {"name": "Системник", "price": 1430, "stock": 99},
    5: {"name": "Навушники", "price": 90, "stock": 99},
}

cart = {}

def format_price(price):
    return f"{price:.2f} грн"

def show_catalog():
    print("\n====== КАТАЛОГ ТОВАРІВ ======")

    for product_id , product in products.items():
        print(
            f"{product_id}. {product['name']} - "
            f"Ціна: {format_price(product['price'])}. "
            f"Залишок: {product['stock']} шт."
        )

def add_to_cart():
    show_catalog()

    try:
        product_id = int(input("\nВведіть номер товару: "))
        quantity = int(input("\nВведіть кількість товару: "))
    except ValueError:
        print("Error404 Translate: Введіть ціле число.")
        return
    if product_id not in products:
        print("Такого товару немає!")
        return
    if quantity <= 0:
        print("Ккількість товару повина бути більше 0!")
        return

    product = products[product_id]
    cart_quantity = cart.get(product_id, 0)

    if cart_quantity + quantity > product['stock']:
        print("Недостатньо товару на складі!")
        return
    cart[product_id] = cart_quantity + quantity

    print(f"Додано до кошика: {product['name']} - {quantity} шт.")

def show_cart():
    print("\n===== КОШИК =====")

    if not cart:
        print("Кошик порожній.")
        return

    total = 0

    for product_id, quantity in cart.items():
        product = products[product_id]
        price = product['price'] * quantity
        total += price

        print(
            f"{product['name']} - "
            f"Кількість: {quantity} шт. "
            f"Сума: {format_price(total)}"
        )

        print("-" * 30)
        print(f"До сплати: {format_price(total)}")

def remove_from_cart():
     show_cart()

     if not cart:
         return

     try:
         product_id = int(input("\nВведіть номер товару для видалення: "))
     except ValueError:
         print("Error404 Translate: Введіть номер товару.")
         return

     if product_id not in cart:
         print("Цього товару немає в кошику!")
         return

     del cart[product_id]

     print("Товар повністю видалено з кошику!")

def buy_products():
    if not cart:
        print("\nКошик порожній.")

    show_cart()

    confirmation = input(
        "\nПідтвердити покупку? так/ні: "
    ).strip().lower()

    if confirmation == "ні":
        print("Покупку скасовано.")
        return

    elif confirmation == "так":
        for product_id, quantity in cart.items():
            products[product_id]["stock"] -= quantity

        total = sum(
            products[product_id]["price"] * quantity
            for product_id, quantity in cart.items()
        )

        print("\nПокупку здійснено успішно!")
        print(f"Сума покупки: {format_price(total)}")

        cart.clear()

    else:
        print("Невірна відповідь! Введіть: 'так' або 'ні'.")

def admin_login():
    L = input("Логін: ")
    P = input("Пароль: ")

    if L == "Bbom3331" and P == "Forget415":
        print("\nВхід успішний!")
        return True

    print("Невірний логін або пароль!")
    return False

def show_stock():
    print("\n===== ЗАЛИШОК НА СКЛАДІ =====")

    for product_id, product in sorted(
        products.items(),
        key=lambda item: item[1]['stock']
    ):
        print(
            f"{product['name']} - " 
            f"Залишок: {product['stock']} шт. " 
            f"Ціна: {format_price(product['price'])}"
        )