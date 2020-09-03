def parse(data):
    x = 0
    result = []
    for elem in data:
        if elem == 'i':
            x += 1
        elif elem == 'd':
            x -= 1
        elif elem == 's':
            x **= 2
        elif elem == 'o':
            result.append(x)

    return result
