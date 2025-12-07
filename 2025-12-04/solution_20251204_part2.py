def Check_Open(grid,i,j):
    if i<0 or j < 0 : return False
    try:
        if grid[i][j] == "@" or grid[i][j] == "X":
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

def Remove_Rolls(grid):
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
                grid[i][j] = "X"
    return at_count,grid

def Clear_Space(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j])=="X":
                grid[i][j] = "."
    return grid

at_count = 0
while True:
    new_at_count, grid = Remove_Rolls(grid)
    at_count = at_count + new_at_count
    print(new_at_count)
    grid = Clear_Space(grid)
    if new_at_count == 0: break

print(at_count)