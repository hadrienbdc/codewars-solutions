def calculate_years(principal, interest, tax, desired):
    result = 0

    while principal < desired:
        principal += (principal * interest) * (1-tax)
        print(principal)
        result += 1

    return result
