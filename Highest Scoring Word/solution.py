def high(x):
    ref = 'abcdefghijklmnopqrstuvwxyz'

    max_score_word = 0
    for word in x.split(' '):
        score_word = 0
        for letter in word:
            score_word += (ref.index(letter) + 1)

        if score_word > max_score_word:
            max_score_word = score_word
            result = word

    return result
