#dial numbers 0 - 99
#starts at 50

def Left_Turn(dial,move):
    if int(move[1:]) <= dial:
        return dial-(int(move[1:]))
    else:
        move = "L" + str(int(move[1:])-dial)
        dial = 100
        return Left_Turn(dial,move)


def Right_Turn(dial,move):
    if int(move[1:]) <= (99-dial):
        return dial+(int(move[1:]))
    else:
        move = "R" + str(int(move[1:])-(99-dial))
        dial = 0
        return Right_Turn(dial,move)
    
f = open("C:\\Users\\Zoop\\Desktop\\SDE Learning\\git\\adventofcode\\2025-12-01\\Input.txt")
dial = 50
count = 0
for line in f:
    line = line.strip()
    if line[0:1]=="L":
        dial = Left_Turn(dial,line)
    if line[0:1]=="R":
        dial = Right_Turn(dial,line)
    if(dial==0): count = count+1
    print(line + " - " + str(dial) + " - " + str(count))
print(count)

#right turning to 0 instead of 99 