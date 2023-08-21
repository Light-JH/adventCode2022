import numpy as np

file = open('input.txt', 'r')

knots = list()
tailPos = set()

for i in range(10):
    knots.append((0, 0))

for line in file.readlines():
    [dir, steps] = line.strip().split()
    steps = int(steps)
    if dir == "R":
        for i in range(steps):
            print(knots)
            x, y = knots[0]
            knots[0] = (x, y + 1)
            for k in range(1, len(knots)):
                knot = knots[k]
                delX, delY = knots[k-1][0]-knots[k][0], knots[k-1][1]-knots[k][1]
                if max(abs(delX), abs(delY)) > 1:
                    knots[k] = (knots[k][0] + np.sign(delX), knots[k][1] + np.sign(delY))
                    if knots[k] != (x, y):
                        print(f"failed - {knots}")
                        print(f"knot {k} - {knots[k]} != ({x}, {y})")
                        exit(1)
                x, y = knot
            tailPos.add(knots[-1])

    if dir == "L":
        for i in range(steps):
            x, y = knots[0]
            knots[0] = (x, y - 1)
            for k in range(1, len(knots)):
                delX, delY = knots[k-1][0]-knots[k][0], knots[k-1][1]-knots[k][1]
                if max(abs(delX), abs(delY)) > 1:
                    knots[k] = (knots[k][0] + np.sign(delX), knots[k][1] + np.sign(delY))
            tailPos.add(knots[-1])

    if dir == "U":
        for i in range(steps):
            x, y = knots[0]
            knots[0] = (x + 1, y)
            for k in range(1, len(knots)):
                delX, delY = knots[k-1][0]-knots[k][0], knots[k-1][1]-knots[k][1]
                if max(abs(delX), abs(delY)) > 1:
                    knots[k] = (knots[k][0] + np.sign(delX), knots[k][1] + np.sign(delY))
            tailPos.add(knots[-1])

    if dir == "D":
        for i in range(steps):
            x, y = knots[0]
            knots[0] = (x - 1, y)
            for k in range(1, len(knots)):
                delX, delY = knots[k-1][0]-knots[k][0], knots[k-1][1]-knots[k][1]
                if max(abs(delX), abs(delY)) > 1:
                    knots[k] = (knots[k][0] + np.sign(delX), knots[k][1] + np.sign(delY))
            tailPos.add(knots[-1])

print(len(tailPos))