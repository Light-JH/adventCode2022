file = open('input.txt', 'r')
lines = file.readlines()
Set = set()
count = 0
for line in lines:

    x = line.strip().split(",")
    num1, num2 = int(x[0].split("-")[0]), int(x[0].split("-")[1])
    num3, num4 = int(x[1].split("-")[0]), int(x[1].split("-")[1])


    # if (num1 <= num3 and num2 >= num4):
    #     left, right = num3, num4
    #     print(num1, num2, num3, num4)
    # elif (num1 >= num3 and num2 <= num4):
    #     left, right = num1, num2
    #     print(num1, num2, num3, num4)
    # elif num1 > num3 and num2 > num4:
    #     left, right = num1, num4
    #     print(num1, num2, num3, num4)
    # elif num1 < num3 and num2 < num4:
    #     left, right = num3, num2
    #     print(num1, num2, num3, num4)
    if (num1 > num4 or num2 < num3):
        continue

    count += 1

print(count)