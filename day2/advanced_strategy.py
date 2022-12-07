#A for Rock, B for Paper, and C for Scissors
#X for Rock, Y for Paper, and Z for Scissors
#1 for Rock, 2 for Paper, and 3 for Scissors
#0 if you lost, 3 if the round was a draw, and 6 if you won
#X means you search to lose, Y means you search to end the round in a draw, and Z means you search to win


def choice(opponent, you):
    if opponent == "A":
        if you == "X":
            return 3 #pick scissors
        elif you == "Y":
            return 1  # rock
        elif you == "Z":
            return 2  # paper
    elif opponent == "B":
        if you == "X":
            return 1  # rock
        elif you == "Y":
            return 2  # paper
        elif you == "Z":
            return 3  # scissors
    elif opponent == "C":
        if you == "X":
            return 2  # paper
        elif you == "Y":
            return 3  # scissors
        elif you == "Z":
            return 1  # rock

total_score = 0
with open("rockpaperscissors.txt") as f:
    for line in f:
        your_turn = line.strip()[-1]
        opponent = line.strip()[0]
        if your_turn == "X":
            total_score += 0
            total_score += choice(opponent, your_turn)
        elif your_turn == "Y":
            total_score += 3
            total_score += choice(opponent, your_turn)
        elif your_turn == "Z":
            total_score += 6
            total_score += choice(opponent, your_turn)
        print(total_score)

print("final", total_score)