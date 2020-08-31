def calculate_years(principal, interest, tax, desired):
    result = 0

    while principal < desired:
        principal += (principal * interest) * (1-tax)
        result += 1

    return result
