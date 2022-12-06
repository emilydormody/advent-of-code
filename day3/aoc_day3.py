file = open("day3.txt", "r")
total = 0

lst = file.readlines()
for i in range(len(lst)):
    ruck = lst[i][:len(lst[i])//2]
    sack = lst[i][len(lst[i])//2:]
    for char in ruck:
        for x in sack:
            if char == x:
                lst[i] = char

for x in lst:
    if ord(x) >= 97 and ord(x) <= 122:
        total += ord(x) - 96
    elif ord(x) >= 65 and ord(x) <= 90:
        total += ord(x) - 38

print(total)