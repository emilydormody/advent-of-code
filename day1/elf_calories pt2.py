most = []
max2 = 0
max3 = 0
current_cals = 0
with open("elf_calories.txt") as f:
    for line in f:
        if line.strip() == "":
            most.append(current_cals)
            current_cals = 0
        else:
            current_cals += int(line)

max1= max(most)
most.remove(max1)
max2 = max(most)
most.remove(max2)
max3 = max(most)
print(max1+max2+max3)
