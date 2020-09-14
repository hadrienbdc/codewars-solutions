def balanced_parens(n):
    final_res = [['']]
    for i in range(1, n+1):
        res = []
        for j in range(i):
            for x in final_res[j]:
                for y in final_res[i-j-1]:
                    res.append('(' + x + ')' + y)
        final_res.append(res)

    return final_res[n]
