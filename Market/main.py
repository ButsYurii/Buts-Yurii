from random import choice
from shop import (
    show_catalog,
    add_to_cart,
    show_cart,
    remove_from_cart,
    buy_products,
    admin_login,
    show_stock,
)

while True:
    print("\n====== Holly Shop ======")
    print("1. Переглянути каталог.")
    print("2. Добавити в кошик.")
    print("3. Переглянути кошик.")
    print("4. Видалити товар з кошику.")
    print("5. Купити кошик.")
    print("6. Ввійти як адміністратор.")
    print("0. Покинути магазин.")

    choice = input("Виберіть дію: ")

    if choice == "1":
        show_catalog()

    elif choice == "2":
        add_to_cart()

    elif choice == "3":
        show_cart()

    elif choice == "4":
        remove_from_cart()

    elif choice == "5":
        buy_products()

    elif choice == "6":
        if admin_login():
            show_stock()

    elif choice == "0":
        print("Дякуєм за візит!")
        break

    else:
        print("Невірний пункт меню. Спробуйте ще раз!")