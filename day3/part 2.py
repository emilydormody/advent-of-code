
file = open("day3.txt", "r")
total = 0
lst = file.readlines()
doubles = []

def ord_check(x):
    if ord(x) >= 97 and ord(x) <= 122:
        return ord(x) - 96
    elif ord(x) >= 65 and ord(x) <= 90:
        return ord(x) - 38
    return "here"

for i in range(0,len(lst),3):
    ruck = lst[i].strip()
    sack = lst[i+1].strip()
    three = lst[i+2].strip()

    for char in ruck:
        if char in sack and char in three:
            total += ord_check(char)
            break

file.close()

print(total)