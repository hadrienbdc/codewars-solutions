def get_middle(s):
    len_s = len(s)
    middle = len_s / 2
    if len_s % 2 == 0:
        result = s[int(middle)-1: int(middle)+1]
    else:
        result = s[int(middle)]

    return result
