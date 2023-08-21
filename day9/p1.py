file = open('input.txt', 'r')

x, y = 0, 0
a, b = 0, 0
pos = list()

for line in file.readlines():
    [dir, steps] = line.strip().split()
    steps = int(steps)
    if dir == "R":
        for i in range(steps):
            y += 1
            delX, delY = abs(x-a), abs(y-b)
            if max(delX, delY) >= 2:
                a, b = x, y - 1
            pos.append((a,b))

    if dir == "L":
        for i in range(steps):
            y -= 1
            delX, delY = abs(x-a), abs(y-b)
            if max(delX, delY) >= 2:
                a, b = x, y + 1
            pos.append((a,b))
    if dir == "U":
        for i in range(steps):
            x += 1
            delX, delY = abs(x-a), abs(y-b)
            if max(delX, delY) >= 2:
                a, b = x - 1, y
            pos.append((a,b))

    if dir == "D":
        for i in range(steps):
            x -= 1
            delX, delY = abs(x-a), abs(y-b)
            if max(delX, delY) >= 2:
                a, b = x + 1, y
            pos.append((a,b))
# print(len(pos), pos)
# print(pos)
pos = set(pos)
print(len(pos))