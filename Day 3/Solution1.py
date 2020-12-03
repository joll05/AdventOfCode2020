f=open("input.txt")
Input = f.read().split("\n")
f.close()

x=0
y=0
count=0
while(y < len(Input)):
    count += Input[y][x%len(Input[0])] == "#"
    x += 3
    y += 1

print(count)
