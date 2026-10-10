from catalog import products as pr, show_catalog as sc
from search import search_products as sp
from cart import add_to_cart as atc
from add_product import add_product as ap
from remove_product import remove_product as rp
from calculate_total import calculate_total as ct
from sort_products import sort_products as srt
from filter_protucts import filter_products as fp
from show_product import show_product as shp
from discount import calculate_discount as cd
from statistics import get_statistics as gs
from validate import validate_product as vp
from export_data import export_products as ep
from import_data import import_products as ip
from history import add_history as ah, history as hist


def show_menu():
    """Виводить головне меню магазину."""
    print("\n========== HOLLYSHOP ==========")
    print("1. Переглянути каталог")
    print("2. Знайти товар")
    print("3. Додати товар до кошика")
    print("4. Додати новий товар")
    print("5. Видалити товар")
    print("6. Розрахувати вартість кошика")
    print("7. Сортувати товари")
    print("8. Фільтрувати товари за ціною")
    print("9. Переглянути товар")
    print("10. Розрахувати знижку")
    print("11. Статистика магазину")
    print("12. Експортувати каталог")
    print("13. Імпортувати каталог")
    print("14. Історія операцій")
    print("0. Вихід")
    print("===============================")


def main():
    """Запускає головний цикл магазину."""
    cart = {}

    while True:
        show_menu()
        choice = input("Вибери дію: ").strip()

        if choice == "1":
            sc()

        elif choice == "2":
            query = input("Введи назву товару: ").strip()
            res = sp(query)

            if res:
                for prod in res:
                    print(
                        f'{prod["id"]}. {prod["name"]} — '
                        f'{prod["price"]:.2f} грн, '
                        f'кількість: {prod["stock"]}'
                    )
            else:
                print("Товарів не знайдено.")

        elif choice == "3":
            try:
                pid = int(input("ID товару: "))
                qty = int(input("Кількість: "))

                old_qty = cart.get(pid, 0)
                new_cart = atc(cart.copy(), pid, qty)

                if new_cart.get(pid, 0) > old_qty:
                    cart = new_cart
                    print("Кошик оновлено.")
                    ah(f"До кошика додано товар ID {pid}")
                else:
                    print(
                        "Не вдалося додати товар. "
                        "Перевір ID, кількість і залишок."
                    )

            except ValueError:
                print("Помилка: введи цілі числа.")

        elif choice == "4":
            name = input("Назва товару: ").strip()

            try:
                price = float(input("Ціна: "))
                stock = int(input("Кількість: "))

                if vp(name, price, stock):
                    if ap(name, price, stock):
                        print("Товар успішно додано.")
                        ah(f"Додано товар: {name}")
                else:
                    print("Некоректні дані товару.")

            except ValueError:
                print("Помилка: перевір введені числа.")

        elif choice == "5":
            try:
                pid = int(input("ID товару для видалення: "))

                if rp(pid):
                    cart.pop(pid, None)
                    print("Товар видалено.")
                    ah(f"Видалено товар ID {pid}")
                else:
                    print("Товар не знайдено.")

            except ValueError:
                print("Помилка: ID має бути цілим числом.")

        elif choice == "6":
            total = ct(cart)
            print(f"Загальна вартість кошика: {total:.2f} грн")

        elif choice == "7":
            direction = input(
                "Сортувати за зростанням? (так/ні): "
            ).strip().lower()

            items = srt(reverse=direction == "ні")

            for pid, prod in items:
                print(
                    f'{pid}. {prod["name"]} — '
                    f'{prod["price"]:.2f} грн'
                )

        elif choice == "8":
            try:
                min_price = float(input("Мінімальна ціна: "))
                max_price = float(input("Максимальна ціна: "))

                if min_price < 0 or max_price < min_price:
                    print("Некоректний діапазон цін.")
                    continue

                res = fp(min_price, max_price)

                for pid, prod in res:
                    print(
                        f'{pid}. {prod["name"]} — '
                        f'{prod["price"]:.2f} грн'
                    )

                if not res:
                    print("Товарів у цьому діапазоні немає.")

            except ValueError:
                print("Помилка: введи коректні ціни.")

        elif choice == "9":
            try:
                pid = int(input("ID товару: "))
                shp(pid)

            except ValueError:
                print("Помилка: ID має бути цілим числом.")

        elif choice == "10":
            try:
                total = float(input("Сума покупки: "))
                percent = float(input("Відсоток знижки: "))

                res = cd(total, percent)

                if res is not None:
                    print(
                        f'Сума знижки: '
                        f'{res["discount_amount"]:.2f} грн'
                    )
                    print(
                        f'До сплати: {res["final_price"]:.2f} грн'
                    )
                else:
                    print("Некоректна сума або відсоток знижки.")

            except ValueError:
                print("Помилка: введи коректні числа.")

        elif choice == "11":
            stats = gs()

            print(f'Видів товарів: {stats["total_products"]}')
            print(f'Одиниць на складі: {stats["total_stock"]}')
            print(
                f'Вартість запасів: '
                f'{stats["total_value"]:.2f} грн'
            )

        elif choice == "12":
            try:
                path = ep()
                print(f"Каталог збережено: {path}")
                ah("Експортовано каталог товарів")

            except OSError as error:
                print(f"Помилка збереження: {error}")

        elif choice == "13":
            data = ip()

            if data is None:
                print("Не вдалося завантажити каталог.")
                continue

            try:
                converted = {
                    int(pid): prod
                    for pid, prod in data.items()
                }

                valid = all(
                    isinstance(prod, dict)
                    and vp(
                        prod.get("name"),
                        prod.get("price"),
                        prod.get("stock"),
                    )
                    for prod in converted.values()
                )

                if valid:
                    pr.clear()
                    pr.update(converted)
                    cart.clear()

                    print("Каталог успішно імпортовано.")
                    ah("Імпортовано каталог товарів")
                else:
                    print("Файл містить некоректні дані.")

            except (TypeError, ValueError):
                print("Не вдалося обробити дані каталогу.")

        elif choice == "14":
            if hist:
                for rec in hist:
                    print(
                        f'{rec["time"]} — {rec["action"]}'
                    )
            else:
                print("Історія операцій порожня.")

        elif choice == "0":
            print("Дякуємо за використання HollyShop!")
            break

        else:
            print("Невідома команда. Спробуй ще раз.")


if __name__ == "__main__":
    main()