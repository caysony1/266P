# Number utility standalone functions

def is_positive (input_value):
    is_valid = input_value is not None and input_value > 0

    if is_valid is False:
        raise ValueError('input number is not positive!')
    
    return True