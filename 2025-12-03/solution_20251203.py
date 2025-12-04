


def Find_Largest(number):
    number = str(number)
    largest = 0
    new_number = ""
    for i in range (len(number)-1):
        if int(number[i])>largest:
            largest = int(number[i])
            new_number= number[i+1:]
    
    largest2 = 0
    for i in range (len(new_number)):
        if int(new_number[i])>largest2:
            largest2 = int(new_number[i])
    return(10*largest+largest2)




f = open("C:\\Users\\Zoop\\Desktop\\SDE Learning\\git\\adventofcode\\2025-12-03\\input.txt")
input_array = []
for line in f:
    input_array.append(line.strip())

sum = 0
for n in input_array:
    sum = sum + Find_Largest(n)

print(sum)