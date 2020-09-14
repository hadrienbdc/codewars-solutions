def perimeter(n):
    arr = [1, 1]
    for i in range(2, n+1):
        arr.append(arr[i-1] + arr[i-2])

    res = 4 * sum(arr)

    return res
