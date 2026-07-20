from django.core.exceptions import ValidationError

def validate_positive_price(value):
    """
    Validator to ensure that the price is greater than or equal to zero.
    """
    if value < 0:
        raise ValidationError("Price must be a positive value.")

def validate_product_stock(stock):
    """
    Validator to ensure that stock is not negative.
    """
    if stock < 0:
        raise ValidationError("Stock cannot be negative.")
