opponent_dict = { "A": 1, "B": 2, "C": 3}
player_dict = { "X": 1, "Y": 2, "Z": 3}

def win(x, y):
    return (x == 1 and y == 2) or (x == 2 and y == 3) or (x == 3 and y == 1)

file1 = open('input.txt', 'r')
lines = file1.readlines()
score = 0
for line in lines:
    opponent = opponent_dict[line[0]]
    player = player_dict[line[2]]

    score += player   # base points for choice
    if opponent == player:
        score += 3    # points for draw
    elif win(opponent, player):
        score += 6    # points for win
print(score)

