f=open("input.txt")
Input=sorted(map(int, f.read().split("\n")))
Input += [Input[-1]+3]
f.close()

differences = {}
lastValue = 0
for i in Input:
    difference = i - lastValue
    if(difference not in differences):
        differences[difference] = 1
    else:
        differences[difference] += 1
    lastValue = i

print(differences)
print(differences[1] * differences[3])
