lst = open("day8.txt", "r").readlines()


count = 0
def right(row,column):
    me = lst[row][column]
    for x in range(column+1, len(lst[0])-1):
        if lst[row][x] >= me:
            return False
    return True

def left(row,column):
    me = lst[row][column]
    for x in range(column):
        if lst[row][x] >= me:
            return False
    return True

def top(row,column):
    me = lst[row][column]
    for x in range(row):
        if lst[x][column] >= me:
            return False
    return True

def bottom(row,column):
    me = lst[row][column]
    for x in range(row+1, len(lst)):
        if lst[x][column] >= me:
            return False
    return True

for i in range(len(lst)):
    for a in range(len(lst[0])-1):
        if left(i,a) or right(i,a) or top(i,a) or bottom(i,a):
            count += 1

print(count)




