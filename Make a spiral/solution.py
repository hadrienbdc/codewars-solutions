def spiralize(size):
    spiral = [[0 for n in range(size)] for n in range(size)]

    pos_x, pos_y = 0, 0
    direction = 'right'
    while True:
        spiral[pos_y][pos_x] = 1
#         show spiral in good format

#         print(direction)
#         print('\n'.join(' '.join(str(x) for x in row) for row in spiral))

        if direction == 'right':
            if pos_x + 1 < size:
                if pos_x + 2 < size:
                    if spiral[pos_y][pos_x + 2] == 1:
                        direction = 'down'
                        pos_y += 1
                        if (spiral[pos_y][pos_x-1] != 0
                           or spiral[pos_y][pos_x+1] != 0
                           or spiral[pos_y+1][pos_x] != 0):
                            break
                    else:
                        pos_x += 1
                else:
                    pos_x += 1
            else:
                direction = 'down'

        elif direction == 'down':
            if pos_y + 1 < size:
                if pos_y + 2 < size:
                    if spiral[pos_y + 2][pos_x] == 1:
                        direction = 'left'
                        pos_x -= 1
                        if (spiral[pos_y-1][pos_x] != 0
                           or spiral[pos_y+1][pos_x] != 0
                           or spiral[pos_y][pos_x-1] != 0):
                            break
                    else:
                        pos_y += 1
                else:
                    pos_y += 1
            else:
                direction = 'left'

        elif direction == 'left':
            if pos_x - 1 >= 0:
                if pos_x - 2 >= 0:
                    if spiral[pos_y][pos_x - 2] == 1:
                        direction = 'up'
                        pos_y -= 1
                        if (spiral[pos_y][pos_x-1] != 0
                           or spiral[pos_y][pos_x+1] != 0
                           or spiral[pos_y-1][pos_x] != 0):
                            break
                    else:
                        pos_x -= 1
                else:
                    pos_x -= 1
            else:
                direction = 'up'

        elif direction == 'up':
            if pos_y - 1 >= 0:
                if pos_y - 2 >= 0:
                    if spiral[pos_y - 2][pos_x] == 1:
                        direction = 'right'
                        pos_x += 1
                        if (spiral[pos_y-1][pos_x] != 0
                           or spiral[pos_y+1][pos_x] != 0
                           or spiral[pos_y][pos_x+1] != 0):
                            break
                    else:
                        pos_y -= 1
                else:
                    pos_y -= 1
            else:
                direction = 'right'

    return spiral
