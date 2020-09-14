import re


def alphanumeric(password):
    if re.search(r'\W|_', password) or password == '':
        return False

    return True
