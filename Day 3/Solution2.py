f=open("input.txt")
Input = f.read().split("\n")
f.close()

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

product = 1
for slope in slopes:
    x=0
    y=0
    count=0
    while(y < len(Input)):
        count += Input[y][x%len(Input[0])] == "#"
        x += slope[0]
        y += slope[1]
    product *= count

print(product)
