file = open('input.txt', 'r')
trees = []

for line in file.readlines():
    trees.append([int(x) for x in line.strip()])

maxview = 0
for row in range(len(trees)):
    #scan from the left
    for col in range(len(trees[row])):
        countLeft = 0
        countRight = 0
        countTop = 0
        countBottom = 0
        for i in reversed(range(col)):
            if trees[row][i] < trees[row][col]:
                countLeft += 1
            elif trees[row][i] >= trees[row][col]:
                countLeft += 1
                break
        for j in range(col+1, len(range(len(trees)))):
            if trees[row][j] < trees[row][col]:
                countRight += 1
            elif trees[row][j] >= trees[row][col]:
                countRight += 1
                break
        for k in reversed(range(row)):
            if trees[k][col] < trees[row][col]:
                countTop += 1
            elif trees[k][col] >= trees[row][col]:
                countTop += 1
                break
        for l in range(row+1, len(trees)):
            if trees[l][col] < trees[row][col]:
                countBottom += 1
            elif trees[l][col] >= trees[row][col]:
                countBottom += 1
                break
        # print(f"({row}, {col}): [{countLeft}, {countRight}, {countTop}, {countBottom}]")
        view = countLeft*countRight*countTop*countBottom

        if view > maxview:
            maxview = view
print(maxview)






