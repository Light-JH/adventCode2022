opponent_dict = { "A": 1, "B": 2, "C": 3}
result_dict = { "X": 0, "Y": 3, "Z": 6}
to_win = {1 : 2, 2:3, 3:1}
to_lose = {1:3, 2:1, 3:2}


file1 = open('input.txt', 'r')
lines = file1.readlines()
score = 0
for line in lines:
    opponent = opponent_dict[line[0]]
    score1 = result_dict[line[2]]

    score += score1
    if score1 == 0:
        score += to_lose[opponent]
    elif score1 == 6:
        score += to_win[opponent]
    else:
        score += opponent
print(score)

