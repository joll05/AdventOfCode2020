import re

f=open("input.txt")
Input = f.read().split("\n")
f.close()

regex = r"(.+)-(.+) (.): (.+)"

count = 0
for i in Input:
    match = re.match(regex, i)
    pos1 = int(match.group(1)) - 1
    pos2 = int(match.group(2)) - 1
    char = match.group(3)
    password = match.group(4)

    if((password[pos1] + password[pos2]).count(char) == 1):
        count += 1

print(count)
