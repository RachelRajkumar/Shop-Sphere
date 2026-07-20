def format_price_currency(amount, currency_symbol="$"):
    """
    Format a decimal amount to a standard currency string.
    """
    try:
        return f"{currency_symbol}{float(amount):.2f}"
    except (ValueError, TypeError):
        return f"{currency_symbol}0.00"


def calculate_discounted_price(original_price, discount_percentage):
    """
    Calculate the price after applying a discount percentage.
    """
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    
    discount_amount = float(original_price) * (discount_percentage / 100)
    return max(0.0, float(original_price) - discount_amount)
