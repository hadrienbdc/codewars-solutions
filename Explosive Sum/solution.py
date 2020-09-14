def exp_sum(n):
    if n < 0:
        return 0

    arr = [1] + [0] * n

    for i in range(1, n+1):
        for j in range(i, n+1):
            arr[j] += arr[j-i]

    res = arr[-1]

    return res
