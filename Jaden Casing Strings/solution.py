def to_jaden_case(string):
    result = " ".join([char[0].upper() + char[1:] for char in string.split(' ')])

    return result
