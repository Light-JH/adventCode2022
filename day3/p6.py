import string
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
   values[letter] = index + 27

file = open('input.txt', 'r')
lines = file.readlines()
sum = 0
badget = []
Set = set()

for index, line in enumerate(lines):
    if index % 3 == 0:
        if len(Set) > 0: badget.append(list(Set)[0])
        Set = set([x for x in line.strip()])
    else:
        Set = Set.intersection(set([x for x in line.strip()]))

for i in range(len(badget)):
    sum += values[badget[i]]
print(sum)




