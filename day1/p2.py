
import heapq

file1 = open('input.txt', 'r')
lines = file1.readlines()
maxThree = []
# heapq.heapify(maxThree)
sum = 0
for line in lines:
    if line != "\n":
        sum += int(line)

    if line == "\n":

        if len(maxThree) == 3 and sum > maxThree[0]:
            heapq.heappop(maxThree)
            heapq.heappush(maxThree, sum)
        elif len(maxThree) < 3:
            heapq.heappush(maxThree, sum)
        sum = 0
sum = 0
for i in range(len(maxThree)):
    sum += maxThree[i]
    print(maxThree[i])
print(sum)






