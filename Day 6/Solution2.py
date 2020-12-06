f=open("input.txt")
Input=f.read().split("\n\n")
f.close()

total = 0
for group in Input:
    members = group.split("\n")
    answers = {}
    for member in members:
        for c in member:
            if(c not in answers): answers[c] = 1
            else: answers[c] += 1

    for a in answers:
        if(answers[a] == len(members)): total += 1

print(total)
