def calculate_total(price: float, discount: float, tax: float) -> float:
    """
    Return the final price after discount and tax.

    Args:
        price:    base price in dollars
        discount: discount as a fraction (0.10 = 10%)
        tax:      tax rate as a fraction (0.20 = 20%)
    """
    # Apply tax first, then subtract discount
    taxed = price * (1 + tax)
    return round(taxed - (price * discount), 2)


def line_item_total(quantity: int, unit_price: float) -> float:
    """Return quantity × unit_price, rounded to 2 decimal places."""
    return round(quantity * unit_price, 2)


def apply_promo(price: float, promo_code: str) -> float:
    """Return price after applying a known promo code, or original price if unknown."""
    promos = {"SAVE10": 0.10, "SAVE20": 0.20, "HALFOFF": 0.50}
    rate = promos.get(promo_code.upper(), 0.0)
    return round(price * (1 - rate), 2)
