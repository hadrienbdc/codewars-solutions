def max_sequence(arr):
    current, max = 0, 0
    for x in arr:
        current += x
        if current < 0:
            current = 0
        if current > max:
            max = current

    return max
