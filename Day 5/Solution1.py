f=open("input.txt")
Input=f.read().split("\n")
f.close()

highestID = 0
for p in Input:
    p = p.replace("F", "0")
    p = p.replace("B", "1")
    p = p.replace("L", "0")
    p = p.replace("R", "1")

    row = int(p[:7], 2)
    col = int(p[7:], 2)
    ID = row * 8 + col
    if(ID > highestID):
        highestID = ID

print(highestID)
