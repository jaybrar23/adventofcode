def Check_List_Of_Number(split_number):
    start = split_number[0]
    for i in split_number[1:]:
        if i != start: return False
        start = i
    return True

def Split_Num(num,i):
    num = str(num)
    list = []
    for x in range (0, len(num),i):
        list.append((num[x:x+i]))
    return list

def Check_Number(num):
    noOfDigits = len(str(num))
    for j in range(1,noOfDigits):
        if noOfDigits%j == 0:
            split_number = Split_Num(num,j)
            if Check_List_Of_Number(split_number) == True:
                return True

def Check_Invalid(sequence):
    sum = 0
    start,finish = sequence.split("-")
    start = int(start)
    finish = int(finish)
    for i in range (start,finish+1):
        if Check_Number(i) == True:
            sum = sum + i
    return sum

f = open("C:\\Users\\Zoop\\Desktop\\SDE Learning\\git\\adventofcode\\2025-12-02\\input.txt")
input_array = []
for line in f:
    input_array = line.split(",")

sum = 0
for sequence in input_array:
    sum = sum + Check_Invalid(sequence)

print(sum)
