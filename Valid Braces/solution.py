def validBraces(string):
    match = {')': '(', '}': '{', ']': '['}

    stack = []
    for char in string:
        if char in match.values():
            stack.append(char)
        else:
            if len(stack) > 0 and match[char] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return False

    if stack:
        return False
    else:
        return True
