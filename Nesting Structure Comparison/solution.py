def same_structure_as(original, other):
    if type(original) != type(other):
        return False
    if len(original) != len(other):
        return False
    else:
        for i in range(len(original)):
            if isinstance(original[i], list):
                if isinstance(other[i], list):
                    return same_structure_as(original[i], other[i])
                else:
                    return False
            else:
                if isinstance(other[i], list):
                    return False

        return True
