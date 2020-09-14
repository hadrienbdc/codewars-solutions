def recoverSecret(triplets):
    unique = triplets[0][:]
    for triplet in triplets:
        for l in triplet:
            if l not in unique:
                unique.append(l)

    for triplet in triplets:
        fix(unique, triplet[0], triplet[1])
        fix(unique, triplet[1], triplet[2])

    for triplet in triplets:
        fix(unique, triplet[0], triplet[1])

    res = ''.join(unique)

    return res


def fix(l, a, b):
    if l.index(a) > l.index(b):
        l.remove(a)
        l.insert(l.index(b), a)
