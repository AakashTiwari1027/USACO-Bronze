#easy floodfill problem, no catch

import sys
sys.stdin = open('cowart.in','r')
sys.stdout = open('cowart.out','w')
sys.setrecursionlimit(2**30)
n = int(input())
painting = [list(input()) for i in range(n)]

visted = [[False for i in range(n)] for j in range(n)]
def floodfill(x,y,color):
    visted[y][x] = True
    dir = [[0,1],[1,0],[0,-1],[-1,0]]
    for i in dir:
        if 0 <= x+i[0] < n and 0 <= y+i[1] < n:
            if visted[y+i[1]][x+i[0]] == False and painting[y+i[1]][x+i[0]] == color:
                floodfill(x+i[0],y+i[1],color)
    
human = 0
for y in range(n):
    for x in range(n):
        if visted[y][x] == False:
            human+=1
            floodfill(x,y,painting[y][x])

for y in range(n):
    for x in range(n):
        if painting[y][x] == 'G':
            painting[y][x] = 'R'

cow = 0
visted = [[False for i in range(n)] for i in range(n)]
for y in range(n):
    for x in range(n):
        if visted[y][x] == False:
            cow+=1
            floodfill(x,y,painting[y][x])

print(human,cow)