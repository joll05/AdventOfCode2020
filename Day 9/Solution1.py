f=open("input.txt")
Input=list(map(int, f.read().split("\n")))
f.close()

for i in range(25, len(Input)):
    previousNumbers = Input[i-25:i]
    valid = False
    for n1 in previousNumbers:
        for n2 in previousNumbers:
            if(n1 != n2):
                if(n1 + n2 == Input[i]):
                    valid = True

    if(not valid):
        print(Input[i])
