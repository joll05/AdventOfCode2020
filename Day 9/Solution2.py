f=open("input.txt")
Input=list(map(int, f.read().split("\n")))
f.close()

invalidNumber = 0
for i in range(25, len(Input)):
    previousNumbers = Input[i-25:i]
    valid = False
    for n1 in previousNumbers:
        for n2 in previousNumbers:
            if(n1 != n2):
                if(n1 + n2 == Input[i]):
                    valid = True

    if(not valid):
        invalidNumber = Input[i]
        break

for lower in range(0, len(Input)):
    for upper in range(lower + 1, len(Input)):
        if(sum(Input[lower:upper+1]) == invalidNumber):
            print(min(Input[lower:upper+1]) + max(Input[lower:upper+1]))
