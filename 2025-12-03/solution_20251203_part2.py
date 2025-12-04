#12 instead of 2


def Find_Largest(number):
    number = str(number)
    largest_numbers = []
    for i in range(1,13):
        current_largest = 0
        new_start = ""
        for j in range (len(number)-(12-i)):
            if int(number[j])>current_largest:
                current_largest = int(number[j])
                new_start = j
        largest_numbers.append(str(current_largest))
        try:
            number = number[new_start+1:]
        except:
            pass
    return largest_numbers



f = open("C:\\Users\\Zoop\\Desktop\\SDE Learning\\git\\adventofcode\\2025-12-03\\input.txt")
input_array = []
for line in f:
    input_array.append(line.strip())

sum = 0
for n in input_array:
    number = ''.join(Find_Largest(n))
    sum = sum+int(number)

print(sum)