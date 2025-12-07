def Check_Open(grid,i,j):
    if i<0 or j < 0 : return False
    try:
        if grid[i][j] == "@":
            return True
        return False
    except:
        return False

f = open("C:\\Users\\Zoop\\Desktop\\SDE Learning\\git\\adventofcode\\2025-12-04\\input.txt")
grid = []
for line in f:
    row = []
    for char in line.strip():
        row.append(char.strip())
    grid.append(row)

at_count = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if(grid[i][j])==".": continue
        adjacent = 0
        if Check_Open(grid,i-1,j-1):
            adjacent = adjacent + 1
        if Check_Open(grid,i-1,j):
            adjacent = adjacent + 1
        if Check_Open(grid,i-1,j+1):
            adjacent = adjacent + 1
        if Check_Open(grid,i,j-1):
            adjacent = adjacent + 1
        if Check_Open(grid,i,j+1):
            adjacent = adjacent + 1
        if Check_Open(grid,i+1,j-1):
            adjacent = adjacent + 1
        if Check_Open(grid,i+1,j):
            adjacent = adjacent + 1
        if Check_Open(grid,i+1,j+1):
            adjacent = adjacent + 1
        if adjacent < 4:
            at_count = at_count+1
print(at_count)

