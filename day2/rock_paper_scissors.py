
#A for Rock, B for Paper, and C for Scissors
#X for Rock, Y for Paper, and Z for Scissors
#1 for Rock, 2 for Paper, and 3 for Scissors
#0 if you lost, 3 if the round was a draw, and 6 if you won

def victory(opponent, you):
    if opponent == "A":
        if you == "X":
            return 3 #draw
        elif you == "Y":
            return 6 #win
        elif you == "Z":
            return 0 #loss
    elif opponent == "B":
        if you == "X":
            return 0 #loss
        elif you == "Y":
            return 3 #draw
        elif you == "Z":
            return 6  # win
    elif opponent == "C":
        if you == "X":
            return 6  # win
        elif you == "Y":
            return 0 #loss
        elif you == "Z":
            return 3  # draw


total_score = 0
with open("rockpaperscissors.txt") as f:
    for line in f:
        your_turn = line.strip()[-1]
        opponent = line.strip()[0]
        if your_turn == "X":
            total_score += 1
            total_score += victory(opponent, your_turn)
        elif your_turn == "Y":
            total_score += 2
            total_score += victory(opponent, your_turn)
        elif your_turn == "Z":
            total_score += 3
            total_score += victory(opponent, your_turn)

print(total_score)