from collections import deque


file = open('input.txt', 'r')

directory_sizes = list()
stack = deque([0])
last_line_cd = False
for line in file.readlines():
    if last_line_cd:
        if "ls" not in line:
            print(line)
        assert("ls" in line)
    if "cd .." in line:
        # Pop from our stack
        directory_size = stack.pop()

        directory_sizes.append(directory_size)

        # Add to the outer directories size
        stack[-1] += directory_size
    elif "$ cd" in line:
        # Push new directory and 0 to the stack
        stack.append(0)
        last_line_cd = True
        continue
    elif "dir" not in line and "$" not in line:
        # Add file size to the current directory size
        spline = line.split()
        size = int(spline[0])
        stack[-1] += size
    # Set this to false...
    last_line_cd = False

while True:
    if len(stack) == 1: break
    directory_size = stack.pop()
    directory_sizes.append(directory_size)
    # Add to the outer directories size
    stack[-1] += directory_size

used_space = stack[-1]
limit = 30000000 - (70000000 - used_space)
valid_dirs = []
for directory_size in directory_sizes:
    if directory_size >= limit:
        valid_dirs.append(directory_size)


print(min(valid_dirs))
