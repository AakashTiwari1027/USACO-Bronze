#we got the solution pretty easily, i mean the only way to do this problem was coordinate compression
#but the implementation was pretty weird
#first of all, they gave the input in the format of p1,p2 on a single line, which threw me off for a bit, what i needed to do was to coordinate compress all the x,y pairs
#coordinate compressing itself was also weird,
#after that we ran into an issue of how to respresent the acutall graph as a 2d array
#representing a x,y point as a element in the array didnt work
#so i tried making every element the gap between x and x+1, that didnt work either
#what i needed to do was add a intermediate, .5 row and collumn
#all in all, pretty bad implemenatation, but got the prob


import sys
sys.stdin = open('crazy.in','r')
sys.stdout = open('crazy.out','w')
sys.setrecursionlimit(2**30)
n,c = map(int,input().split())
fences = [list(map(int,input().split())) for i in range(n)]
cows = [list(map(int,input().split())) for i in range(c)]
dic = {}
for i in range(n):
    dic[(fences[i][0],fences[i][1])] = dic.get((fences[i][0],fences[i][1]),[])+[['F',i,0]]
    dic[(fences[i][2],fences[i][3])] = dic.get((fences[i][2],fences[i][3]),[])+[['F',i,2]]
for i in range(c):
    dic[(cows[i][0],cows[i][1])] = dic.get((cows[i][0],cows[i][1]),[])+[['C',i]]


def compress():
    vals = list(dic.keys())
    compressed_vals = [[0,0] for i in range(len(vals))]
    x,y = {},{}
    for i in range(len(vals)):
        x[vals[i][0]] = x.get(vals[i][0],[])+[i]
        y[vals[i][1]] = y.get(vals[i][1],[])+[i]

    xkeys = sorted(list(x.keys()))
    for i in range(len(xkeys)):
        for j in x[xkeys[i]]:
            compressed_vals[j][0] = i
    
    ykeys = sorted(list(y.keys()))
    for i in range(len(ykeys)):
        for j in y[ykeys[i]]:
            compressed_vals[j][1] = i
    
    for i in range(len(vals)):
        for code in dic[vals[i]]:
            if code[0] == 'F':
                fences[code[1]][code[2]] = compressed_vals[i][0]
                fences[code[1]][code[2]+1] = compressed_vals[i][1]
            if code[0] == 'C':
                cows[code[1]] = compressed_vals[i]
compress()
size = 2*(n+c+1)
grid = [[0 for i in range(size)] for i in range(size)]
#draw fences
for i in fences:
    for j in range(min(i[0],i[2])*2,max(i[0],i[2])*2+1):
        grid[i[1]*2][j] = 1
    for j in range(min(i[1],i[3])*2,max(i[1],i[3])*2+1):
        grid[j][i[0]*2] = 1
for i in cows:
    grid[i[1]*2][i[0]*2] = 2

count = 0
visted = [[False for i in range(size)] for i in range(size)]
def floodfill(x,y):
    global count
    visted[y][x] = True
    if grid[y][x] == 2:
        count+=1
    dir = [[0,1],[0,-1],[1,0],[-1,0]]
    for i in dir:
        if 0 <= x+i[0] < size and 0 <= y+i[1] < size and visted[y+i[1]][x+i[0]] == False and grid[y+i[1]][x+i[0]] != 1:
            floodfill(x+i[0],y+i[1])

ans = []
for y in range(size):
    for x in range(size):
        if visted[y][x] == False and grid[y][x] != 1:
            count = 0
            floodfill(y,x)
            ans.append(count)
print(max(ans))