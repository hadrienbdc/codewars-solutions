def score(dice):
    score = 0
    counter = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for n in dice:
        counter[n] += 1

    print(counter)
    for key, count in counter.items():
        if count >= 3:
            count += -3
            if key == 1:
                score += 1000
            else:
                score += key * 100

        if count >= 1:
            if key == 1:
                score += 100 * count
            if key == 5:
                score += 50 * count

    return score
