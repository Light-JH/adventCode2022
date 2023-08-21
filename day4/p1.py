file = open('input.txt', 'r')
lines = file.readlines()

count = 0
for line in lines:
    x = line.strip().split(",")
    num1, num2 = int(x[0].split("-")[0]), int(x[0].split("-")[1])
    num3, num4 = int(x[1].split("-")[0]), int(x[1].split("-")[1])


    if (num1 <= num3 and num2 >= num4) or  (num1 >= num3 and num2 <= num4):
        count += 1
        print(num1, num2, num3, num4, count)

print(count)





