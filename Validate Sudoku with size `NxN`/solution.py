class Sudoku(object):
    def __init__(self, data):
        self.data = data

    def is_valid(self):
        n = len(self.data)

        test_dim = n ** 0.5

        if not test_dim.is_integer():
            return False

        for row in self.data:
            if len(row) != n:
                return False

        sum_max = n * (n+1) / 2
        count_row = dict(zip(range(n), [0 for i in range(n)]))
        count_col = dict(zip(range(n), [0 for i in range(n)]))
        count_square = dict(zip(range(n), [0 for i in range(n)]))
        for i in range(n):
            for j in range(n):
                elem = self.data[i][j]
                if not isinstance(elem, int):
                    return False
                else:
                    if isinstance(elem, bool):
                        return False
                    else:
                        if elem > n:
                            return False

                count_col[j] += elem
                count_row[i] += elem
                count_square[test_dim * int(i//test_dim) + int(j//test_dim)] += elem

        for v1, v2, v3 in zip(count_row.values(), count_col.values(), count_square.values()):
            if v1 != sum_max or v2 != sum_max or v3 != sum_max:
                return False

        return True
