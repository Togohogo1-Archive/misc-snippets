def printh():
    tmp = []

    for i in ["TL", "TR", "BL", "BR"]:
        if i in hands:
            tmp.append(i)
        else:
            tmp.append("  ")

    print(tmp[0] + "  " + tmp[1] + "\n")
    print(tmp[3] + "  " + tmp[2])

chant = 16
hands = ["TL", "TR", "BR", "BL"]

start = input("First hand slapped: ")

for i in range(10):
    colour = input("Pick a colour: ")
    idx = (hands.index(start) + chant + len(colour))%4
    # assuming only clockwise for now
    print(hands[idx])
printh()
'''
after getting the index of the slapp (after colour):
    the next move is executed by the next avail hand
    the next slapped hand that chooses a colour will be (idx+2) % 4 <- yet to be confirmed
'''
