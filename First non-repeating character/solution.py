def first_non_repeating_letter(string):
    single = []
    duplicate = []
    for char in string.lower():
        print(char)
        if char in duplicate:
            if char in single:
                single.remove(char)
        else:
            single.append(char) 

        duplicate.append(char)

    if single:
        idx = string.lower().index(single[0])
        return string[idx]
    else:
        return ''
