from collections import Counter
from itertools import combinations as c
from pprint import pprint
from math import log2


guesses = [
(1, 2, 3, 4),(4, 13, 14 ,15),(3, 12, 14, 15),(3, 10, 11, 15)
]
matches = [1, 1, 2, 3]
combos = list(c(range(1, 16), 3))
possible_guesses = list(c(range(1, 16), 4))
pool = []

# https://github.com/Togohogo1/Mathtermind/blob/main/classes/classic_solver.py
def solve(pool):
    sols = []

    for cb in pool:
        for rnd, mt in zip(guesses, matches):
            cnt = sum((Counter(cb) & Counter(rnd)).values())

            if cnt != mt:
                break
        else:
            sols.append(cb)

    return sols


pool = solve(combos)


def expected_entropy(guess, pool):
    tot = 0

    for i in range(4):
        prob = p(guess, i, pool)
        tot += 0 if prob == 0 else prob*log2(1/prob)

    return tot


def p(guess, theor_mt, pool):
    tot = 0

    for cb in pool:
        tot += theor_mt == sum((Counter(cb) & Counter(guess)).values())

    return tot/len(pool)

entropies = []
for cb in possible_guesses:
    entropies.append([expected_entropy(cb, pool), cb])
entropies.sort(reverse=True)
pprint(entropies[0][1])

# print(expected_entropy([1, 5], pool))


# print(solve())

