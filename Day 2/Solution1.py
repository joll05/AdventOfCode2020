import re

f=open("input.txt")
Input = f.read().split("\n")
f.close()

regex = r"(.+)-(.+) (.): (.+)"

count = 0
for i in Input:
    match = re.match(regex, i)
    minOccurrence = int(match.group(1))
    maxOccurrence = int(match.group(2))
    char = match.group(3)

    if(minOccurrence <= match.group(4).count(char) <= maxOccurrence):
        count += 1

print(count)
