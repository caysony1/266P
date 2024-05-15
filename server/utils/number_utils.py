# Number utility standalone functions

'''
Changelog:
    05/15/24 - Returns input_value if it passes validation instead of None.

'''


def is_positive(input_value):
    """
    Check if input_value is positive
    Args:
        input_value: Type[Str] or Type[Float]

    Returns:
        input_value
    """
    if input_value is not None and input_value < 0:
        raise ValueError('input number is not positive!')
    else:
        return input_value
