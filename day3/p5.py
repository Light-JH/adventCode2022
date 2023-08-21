import string
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
   values[letter] = index + 27

file = open('input.txt', 'r')
lines = file.readlines()

sum = 0
for line in lines:
    first_half = line[:len(line)//2]
    second_half = line[len(line)//2:]

    first_set = set([x for x in first_half])
    second_set = set([x for x in second_half])

    common_letters = first_set.intersection(second_half)

    for letter in common_letters:
        sum += values[letter]
print(sum)




