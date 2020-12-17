import copy

f=open("input.txt")
Input=f.read().split("\n")
f.close()

surrounding = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

seats = [[0 if y=="L" else -1 for y in x] for x in Input]

previousSeats = []
a=0
while(seats != previousSeats):
    previousSeats = copy.deepcopy(seats)
    
    seatsToChange = []
    for x, row in enumerate(seats):
        for y, seat in enumerate(row):
            if(seat == -1): continue
            count=0
            for s in surrounding:
                xpos=x-s[0]
                ypos=y-s[1]
                if(0 <= xpos < len(seats) and 0 <= ypos < len(row)):
                    #print(xpos, ypos)
                    if(seats[xpos][ypos] == 1): count += 1

            if((count >= 4) if seat == 1 else (count == 0)):
                seatsToChange += [(x, y)]

    for s in seatsToChange:
        seat = seats[s[0]][s[1]]
        seats[s[0]][s[1]] = seat ^ 1

print(sum(row.count(1) for row in seats))
