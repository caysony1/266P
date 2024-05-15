# String utility standalone functions

'''
Changelog:
    05/15/24 - Returns input_value if it passes validation instead of None.

'''


def is_not_null_or_empty(input_value):
    """
    Check if string is empty
    Args:
        input_value: Type[Str]

    Returns:
        input_value if not empty.
    """
    if input_value is not None and input_value.strip() == '':
        raise ValueError('null or empty input value detected!')
    else:
        return input_value
