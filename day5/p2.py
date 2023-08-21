from collections import deque

piles = [1]
stacks = [deque()]
# index[0] = 1
for i in range(8):
    piles.append(piles[-1] + 4)
    stacks.append(deque())
# print(f"piles={piles}")

file = open('input.txt', 'r')
lines = file.readlines()

count = 0
for line in lines:
    if "[" in line:
        for index, num in enumerate(piles):
            # print(line, index, num, line[num])
            if line[num] != " ":
                stacks[index].append(line[num])
    else:
        break
    count += 1
move_block = deque()
for line in lines[count+2:]:
    ele = line.split(" ")
    # number of blocks to move
    num = int(ele[1])
    move = int(ele[3]) - 1 # 3
    to = int(ele[5]) -1 # 5
    while num > 0:
        move_block.append(stacks[move].popleft())
        num -= 1

    while move_block:
        stacks[to].appendleft(move_block.pop())
msg = ""
for stack in stacks:
    msg += (stack.popleft())
print(msg)