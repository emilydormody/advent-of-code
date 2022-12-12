lst = open("day8.txt", "r").readlines()


count = 0
def right(row,column):
    me = lst[row][column]
    for x in range(column+1, len(lst[0])-1):
        if lst[row][x] >= me:
            return x - column
    return column

def left(row,column):
    me = lst[row][column]
    for x in range(column):
        if lst[row][x] >= me:
            return column - x
    return column

def top(row,column):
    me = lst[row][column]
    for x in range(row):
        if lst[x][column] >= me:
            return row-x
    return row

def bottom(row,column):
    me = lst[row][column]
    for x in range(row+1, len(lst)):
        if lst[x][column] >= me:
            return x - row
    return row
best = 0
for i in range(len(lst)):
    for a in range(len(lst[0])-1):
        view = left(i,a) * right(i,a) * top(i,a) * bottom(i,a)
        if best < view: best = view

print(best)




