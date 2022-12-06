file = open("day6.txt","r")
read = file.readline()

queue = []
def no_duplicates():
    for x in queue:
        if queue.count(x) > 1:
            return False
    return True

for i in range(len(read)):
    queue.append(read[i])
    if len(queue) > 14:
        queue.pop(0)
        if no_duplicates():
            print(i+1)
            break

