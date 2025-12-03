def Check_Invalid(sequence):
    sum = 0
    start,finish = sequence.split("-")
    start = int(start)
    finish = int(finish)
    for i in range (start,finish+1):
        noOfDigits = len(str(i))
        #first check
        if noOfDigits%2 ==1:
            continue
        #second check
        half = int(noOfDigits/2)
        if str(i)[0:half] == str(i)[half:]:
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
