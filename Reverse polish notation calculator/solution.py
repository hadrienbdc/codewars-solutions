def calc(expr):
    expr_list = expr.split(' ')
    stack = []
    result = 0
    for elem in expr_list:
        if elem.replace('.', '', 1).isdigit():
            stack.append(float(elem))
        else:
            if elem == '+':
                stack.append(stack.pop(-2) + stack.pop())
            elif elem == '-':
                stack.append(stack.pop(-2) - stack.pop())
            elif elem == '*':
                stack.append(stack.pop(-2) * stack.pop())
            elif elem == '/':
                stack.append(stack.pop(-2) / stack.pop())

    if stack:
        result = stack[0]

    return result
