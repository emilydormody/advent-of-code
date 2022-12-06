file = open("cleaning.txt", "r")
count = 0
elf = file.readline()

while elf.strip() != "":

    lst = elf.strip().split(",")

    elf1 = lst[0].split("-")
    elf2 = lst[1].split("-")

    if int(elf1[0]) >= int(elf2[0]) and not int(elf2[1]) < int(elf1[0]):
        count += 1
    elif int(elf2[0]) >= int(elf1[0]) and not int(elf2[0]) > int(elf1[1]):
        count += 1
    elf = file.readline()

print(count)

