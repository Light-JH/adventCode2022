from collections import deque

file = open('input.txt', 'r')
line = file.readline()
marker = deque()
i, j = 0, 0
while (len(marker) < 14):
    char = line[j]
    # print(i, j, char)
    if char not in marker:
        marker.append(char)
        j+=1
    else:
        marker.popleft()
        i+=1
print(j)