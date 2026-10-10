def calculate_discount(total, discount_percent=0):
    """Обчислює суму знижки та кінцеву вартість."""
    if total < 0:
        return None

    if not 0 <= discount_percent <= 100:
        return None

    discount_amount = total * discount_percent / 100
    final_price = total - discount_amount

    return {
        "original_price": round(total, 2),
        "discount_percent": discount_percent,
        "discount_amount": round(discount_amount, 2),
        "final_price": round(final_price, 2),
    }