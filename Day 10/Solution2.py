f=open("input.txt")
Input=sorted(map(int, f.read().split("\n")))
Input = [0] + Input
f.close()

print(Input)

combinationCounts = [1] + [0] * (len(Input) - 1)
for i, value in enumerate(Input):
    for j, adapterValue in enumerate(Input[i+1:], start=i+1):
        if(adapterValue > value + 3):
            break
        combinationCounts[j] += combinationCounts[i]

print(combinationCounts)
