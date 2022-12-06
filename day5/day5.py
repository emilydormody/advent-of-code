file = open("day5.txt", "r")
stacks = [[],[],[],[],[],[],[],[],[]]
line = file.readline()

def move_crate(take, num, put):
    for x in range(num):
        stacks[put-1].insert(0,stacks[take-1].pop(0))

for x in range(8):
    if line[0:2].strip()!= "":
        stacks[0].append(line[1])
    if line[4:6].strip()!= "":
        stacks[1].append(line[5])
    if line[8:10].strip()!= "":
        stacks[2].append(line[9])
    if line[12:14].strip()!= "":
        stacks[3].append(line[13])
    if line[16:18].strip()!= "":
        stacks[4].append(line[17])
    if line[20:22].strip()!= "":
        stacks[5].append(line[21])
    if line[24:26].strip()!= "":
        stacks[6].append(line[25])
    if line[28:30].strip()!= "":
        stacks[7].append(line[29])
    if line[32:34].strip()!= "":
        stacks[8].append(line[33])
    line = file.readline()


lst = file.readlines()

for y in lst:
    if y.strip() != "":
        y= y.split()
        move_crate(int(y[3]),int(y[1]), int(y[5]))

for i in range(len(stacks)):
    print(stacks[i][0], end="")



