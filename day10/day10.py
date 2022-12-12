lst = open("day10.txt","r").readlines()
X = 0
X_lst = [1]

for i in lst:
    if i.strip() == "noop":
        X_lst.append(0)
    else:
        X_lst.append(0)
        X_lst.append(int(i.split()[1]))

for x in range(20,260,40):
    X += sum(X_lst[:x]*x)
print(X)
