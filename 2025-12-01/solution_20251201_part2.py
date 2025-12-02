#dial numbers 0 - 99
#starts at 50

def Left_Turn(dial,move,count):
    if int(move[1:]) <= dial:
        return dial-(int(move[1:])), count
    else:
        move = "L" + str(int(move[1:])-dial)
        if dial!=0: count = count + 1
        dial = 100
        return Left_Turn(dial,move,count)


def Right_Turn(dial,move,count):
    if int(move[1:]) <= (99-dial):
        return dial+(int(move[1:])),count
    else:
        move = "R" + str(int(move[1:])-(100-dial))
        if int(move[1:]) !=0: count = count + 1
        dial = 0
        return Right_Turn(dial,move,count)
    
f = open("C:\\Users\\Zoop\\Desktop\\SDE Learning\\git\\adventofcode\\2025-12-01\\Input.txt")
dial = 50
count = 0
for line in f:
    line = line.strip()
    if line[0:1]=="L":
        dial,count = Left_Turn(dial,line,count)
    if line[0:1]=="R":
        dial,count = Right_Turn(dial,line,count)
    if(dial==0): count = count+1
print(count)

#right turning to 0 instead of 99 