f=open("input.txt")
Input=f.read().split("\n\n")
f.close()

total = 0
for group in Input:
    members = group.split("\n")
    result = ""
    for member in members:
        for c in member:
            if(c not in result): result += c
    total += len(result)

print(total)
