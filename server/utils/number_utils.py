# Number utility standalone functions

'''
Changelog:
    05/15/24 - Returns input_value if it passes validation instead of None.

'''
from decimal import ROUND_HALF_UP, Decimal

def is_positive(input_value):
    """
    Check if input_value is positive
    Args:
        Type[float] or Type[int]

    Returns:
        input_value
    """
    if input_value is not None and (not isinstance(input_value, (float, int)) or input_value < 0):
        raise ValueError('input number is not positive!')
    else:
        return input_value
    
# using StackOverflow answer from here to ensure that proper currency rounding
# is performed: https://stackoverflow.com/a/13463634
def round_currency(value):
    try:
        rounded_value = Decimal(value).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    except Exception:
        raise ValueError('Invalid input for rounding.')
    return float(rounded_value)
