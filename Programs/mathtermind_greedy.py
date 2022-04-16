from collections import Counter
from itertools import combinations as c
from math import log2

guesses = [(1, 2, 3, 4)]
matches = []
pool = list(c(range(1, 16), 3))
possible_guesses = list(c(range(1, 16), 4))

# https://github.com/Togohogo1/Mathtermind/blob/main/classes/classic_solver.py
def solve():
    sols = []

    for cb in pool:
        for rnd, mt in zip(guesses, matches):
            cnt = sum((Counter(cb) & Counter(rnd)).values())

            if cnt != mt:
                break
        else:
            sols.append(cb)

    return sols


# Expected entropy
def E(guess):
    tot = 0

    for i in range(4):
        prob = p(guess, i)
        tot += 0 if prob == 0 else prob*log2(1/prob)

    return tot


# Probability of getting `theor_mt` matches
def p(guess, theor_mt):
    tot = 0

    for cb in pool:
        tot += theor_mt == sum((Counter(cb) & Counter(guess)).values())

    return tot/len(pool)


while True:
    # entropies = []
    max_entropy = 0
    best_answer = []

    matches.append(int(input()))
    pool = solve()

    if len(pool) == 1:
        print(pool[0])
        break

    for cb in possible_guesses:
        new_entropy = E(cb)

        if new_entropy > max_entropy:
            max_entropy = new_entropy
            best_answer = cb

        # entropies.append([E(cb), cb])

    print(best_answer)
    guesses.append(best_answer)
