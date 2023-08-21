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

for line in lines[count+2:]:
    ele = line.split(" ")
    num = int(ele[1]) # 1
    move = int(ele[3]) - 1 # 3
    to = int(ele[5]) -1 # 5
    while num > 0:
        pop = stacks[move].popleft()
        stacks[to].appendleft(pop)
        num -= 1
msg = ""
for stack in stacks:
    msg += (stack.popleft())
print(msg)




# print(stacks)
# for stack,pile in zip(stacks,piles):
#     print(pile, stack)
