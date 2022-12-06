max = 0
current_cals = 0

with open("elf_calories.txt") as f:
    for line in f:
        if line.strip() == "": #line is empty
            if current_cals > max:
                max = current_cals
            current_cals = 0
        else:
            current_cals += int(line)
print(max)