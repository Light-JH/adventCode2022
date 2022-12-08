# read the file line by line until there is blank line
# sum of each block from input
file1 = open('input.txt', 'r')
lines = file1.readlines()
max = 0
sum = 0
for line in lines:
    if line == "\n":
        if max < sum:
            max = sum
        sum = 0

    else:
        sum += int(line)
print(max)






