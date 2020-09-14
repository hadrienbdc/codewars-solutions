def valid_solution(board):

    sum_max = 45
    count_row = dict(zip(range(9), [0 for i in range(9)]))
    count_col = dict(zip(range(9), [0 for i in range(9)]))
    count_square = dict(zip(range(9), [0 for i in range(9)]))

    for i in range(9):
        for j in range(9):
            elem = board[i][j]

            count_col[j] += elem
            count_row[i] += elem
            count_square[3 * int(i//3) + int(j//3)] += elem

    for v1, v2, v3 in zip(count_row.values(), count_col.values(), count_square.values()):
        if v1 != sum_max or v2 != sum_max or v3 != sum_max:
            return False

    return True
