import sys
sys.stdin = open('perimeter.in','r')
sys.stdout = open('perimeter.out','w')
n = int(input())
size = 102
bales = [list(map(int,input().split())) for i in range(n)]
grid = [[0 for i in range(size)] for i in range(size)]
for i in bales:
    grid[i[1]][i[0]] = 1

for y in range(1,size-1):
    for x in range(1,size-1):
        if grid[y][x] == 0 and grid[y-1][x] == 1 and grid[y+1][x] == 1 and grid[y][x+1] == 1 and grid[y][x-1] == 1:
            grid[y][x] = 1
perimeter = 0
for y in range(size):
    for x in range(size):
        if grid[y][x] == 1:
            adj = [[1,0],[-1,0],[0,1],[0,-1]]
            for i in adj:
                if 0 <= y+i[0] < size and 0 <= x+i[1] < size:
                    if grid[y+i[0]][x+i[1]] == 0:
                        perimeter+=1
print(perimeter)