f=open("input.txt")
Input = list(map(int, f.read().split("\n")))
f.close()

for a in Input:
    for b in Input:
        if(a + b == 2020):
            print(a * b)
