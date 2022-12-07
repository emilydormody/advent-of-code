file = open("day7.txt", "r")
line = file.readline().split()

path = []
directories = []

totals = []

while line != []:
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                current = path.pop()
                totals.append(directories.pop())
            else:
                current = line[2]
                directories.append(0)
                path.append(current)
    else:
        if line[0] != "dir":
            for x in range(len(directories)):
                directories[x] += int(line[0])
    line = file.readline().split()

while directories != []:
    totals.append(directories.pop())

counter = 0
for x in totals:
    if x <= 100000:
        counter += x

print("part 1:", counter)

#part2
totals.sort()
for y in totals:
    if y >= 30000000 - (70000000 - max(totals)):
        print("part 2:",y)
        break
