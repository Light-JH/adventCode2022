file = open('input.txt', 'r')
trees = []

for line in file.readlines():
    trees.append([int(x) for x in line.strip()])

visible = set()
for row in range(len(trees)):
    #scan from the left
    maxTree = -1
    for col in range(len(trees[row])):
        if trees[row][col] > maxTree:
            visible.add((row,col))
            maxTree = trees[row][col]

    #scan from the right
    maxTree = -1
    for col in reversed(range(len(trees))):
        if trees[row][col] > maxTree:
            visible.add((row,col))
            maxTree = trees[row][col]

for col in range(len(trees[0])):
    #scan from the top
    maxTree = -1
    for row in range(len(trees)):
        if trees[row][col] > maxTree:
            visible.add((row,col))
            maxTree = trees[row][col]
    #scan from the bottom
    maxTree = -1
    for row in reversed(range(len(trees))):
        if trees[row][col] > maxTree:
            visible.add((row,col))
            maxTree = trees[row][col]
print(len(visible))

