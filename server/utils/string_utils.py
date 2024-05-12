# String utility standalone functions

def is_not_null_or_empty (input_value):
    is_valid = input_value is not None and input_value.strip() != ''

    if is_valid is False:
        raise ValueError('null or empty input value detected!')