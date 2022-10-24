from pprint import pprint
from fractions import Fraction as F
from collections import defaultdict as dd

ROWS = 9
COLS = 10




s = {i:None for i in "xyzabcdef"}
s2 = {i:0 for i in range(9)}
st = "fedcbazyx"
# mat = [[F(0, 1) for _ in range(COLS)] for _ in range(ROWS)]
mat = [[0 for _ in range(COLS)] for _ in range(ROWS)]

sqr = []

left = [
    [(1, "x")],
    [(1, "x"), (1, "d")],
    [(1, "x"), (2, "d")],
    [(1, "y")],
    [(1, "y"), (1, "e")],
    [(1, "y"), (2, "e")],
    [(1, "z")],
    [(1, "z"), (1, "f")],
    [(1, "z"), (2, "f")]
]

right = [
    [(1, "x")],
    [(1, "x"), (1, "d")],
    [(1, "x"), (2, "d")],
    [(1 ,"x"), (1, "a")],
    [(1, "x"), (1, "d"), (1, "b")],
    [(1, "x"), (2, "d"), (1, "c")],
    [(1, "x"), (2, "a")],
    [(1, "x"), (1, "d"), (2, "b")],
    [(1, "x"), (2, "d"), (2, "c")]
]

xyz = [0]*3

for i in range(3):
    sqr.append(list(input().split()))

for i in range(9):
    elem = sqr[i//3][i%3]

    if i // 3 == 0:
        xyz[i%3] = elem

    for coef, let in left[i]:
        mat[i][st.index(let)] += coef

    if elem == "X":
        for coef, let in right[i]:
            mat[i][st.index(let)] -= coef
    else:
        s2[i] = int(elem)
        mat[i][-1] = int(elem)


pprint(mat)

def col_i_zeros(mat, col):
    for r in range(ROWS):
        if mat[r][col] != 0:
            return False

    return True


def elim(mat):
    r = 0
    c = 0

    while c < COLS:
        if col_i_zeros(mat, c):
            c += 1
            continue

        for rr in range(r+1, ROWS):
            if mat[r][c] == 0 and mat[rr][c] != 0:
                mat[r], mat[rr] = mat[rr], mat[r]
                break

        for rr in range(r+1, ROWS):
            if mat[r][c] != 0:
                f = mat[rr][c]/mat[r][c]
                # f = F(mat[rr][c]/mat[r][c])

                for i in range(c, COLS):
                    mat[rr][i] = mat[rr][i] - mat[r][i]*f

        r += 1
        c += 1


def solve(tri):
    tri.reverse()

    for row_i, let1 in enumerate(reversed(st)):
        tmp = []
        rhs = tri[row_i][-1]

        for col, coef in enumerate(tri[row_i][:-1]):
            let2 = st[col]
            if coef != 0:
                if s[let2] != None:
                    print(rhs, s[let2], coef, type(rhs), type(s[let2]), type(coef))
                    rhs -= s[let2]*coef
                else:
                    tmp.append((coef, let2))

        if not tmp:  # Array empty
            # s[let1] = xyz[st.index(let1)]
            s[let1] = int(xyz[row_i]) if row_i < 3 else 0
            s[let1] = s2[row_i]
        elif len(tmp) == 1:
            s[let1] = rhs/tmp[0][0]
            # s[let1] = F(rhs, tmp[0][0])
        else:  # One of a value, the rest are all zeros

            s[let1] = rhs/tmp[0][0]
            # s[let1] = F(rhs, tmp[0][0])
            for coef, let2 in tmp[1:]:
                s[let2] = 0

elim(mat)
pprint(mat)
print(len(mat))
solve(mat)

pprint(s)

ans = [
    s["x"], s["x"]+s["d"], s["x"]+2*s["d"],
    s["y"], s["y"]+s["e"], s["y"]+2*s["e"],
    s["z"], s["z"]+s["f"], s["z"]+2*s["f"]
]


ans = [
    s["x"], s["x"]+s["d"], s["x"]+2*s["d"],
    s["x"]+s["a"], s["x"]+s["d"]+s["b"], s["x"]+2*s["d"]+s["c"],
    s["x"]+2*s["a"], s["x"]+s["d"]+2*s["b"], s["x"]+2*s["d"]+2*s["c"],
]
# f = 1
# for i in ans:
#     f *= i.denominator

# print(f"""
# {f*ans[0]} {f*ans[1]} {f*ans[2]}
# {f*ans[3]} {f*ans[4]} {f*ans[5]}
# {f*ans[6]} {f*ans[7]} {f*ans[8]}
# """)
print(f"""
{ans[0]} {ans[1]} {ans[2]}
{ans[3]} {ans[4]} {ans[5]}
{ans[6]} {ans[7]} {ans[8]}
""")
