f=open("input.txt")
Input=f.read().split("\n")
f.close()

remainingIDs = list(range(128 * 8))
for p in Input:
    p = p.replace("F", "0")
    p = p.replace("B", "1")
    p = p.replace("L", "0")
    p = p.replace("R", "1")

    row = int(p[:7], 2)
    col = int(p[7:], 2)
    ID = row * 8 + col
    remainingIDs.remove(ID)

for ID in remainingIDs:
    if(remainingIDs.count(ID-1) + remainingIDs.count(ID+1) == 0):
        print(ID)
