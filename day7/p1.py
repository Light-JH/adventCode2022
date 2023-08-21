from collections import deque


file = open('input.txt', 'r')

answer = 0
stack = deque([0])
for line in file.readlines():
    if "cd .." in line:
        # Pop from our stack
        directory_size = stack.pop()

        # Check against the limit
        if directory_size <= 100000:
            answer += directory_size
        # Add to the outer directories size
        stack[-1] += directory_size
    elif "$ cd" in line:
        # Push new directory and 0 to the stack
        stack.append(0)
    elif "dir" not in line and "$" not in line:
        # Add file size to the current directory size
        spline = line.split()
        size = int(spline[0])
        stack[-1] += size

while True:
    if len(stack) == 1: break
    directory_size = stack.pop()
    if directory_size <= 100000:
        answer += directory_size
    # Add to the outer directories size
    stack[-1] += directory_size

print(answer)
