def Check_Invalid(sequence,invalid_ids):
    start,finish = sequence.split("-")
    start = int(start)
    finish = int(finish)
    for i in range (start,finish):
        #first check
        if len(str(i))%2 ==1:
            continue
        #second check
        for j in range(((len(str(i)))/2)-1):
            #tbc


f = open("C:\\Users\\Zoop\\Desktop\\SDE Learning\\git\\adventofcode\\2025-12-02\\Input.txt")
for line in f:
    input_array = line.split(",")

invalid_ids = []
for sequence in input_array:
    invalid_ids = Check_Invalid(sequence,invalid_ids)
