#fullll testcases baby
#aight so this one, at first i was gonna binary search and do some weird stuff to simulate but then i was like
#cuh
#just coord compress and 2d grid
#i did that, implemented it fine, but got like 2 tc
#everything else was wrong
#i though "nice, good debugging practice"
#i debugged, but nothing was working till i found one thing, that i thought of doing while problem solving but ignored while implementation
#we need to feed 0,0 into the coordinate compression
#i thought of that
#BUT I DIDNT DO THE SECOND STEP OF USING THE COMPRESSED 0,0 VALUES IN MY CODE
#i think i did it cuz i thought compressed 0,0 would to to 0,0
#and it would have if not for negative numbers
#so yeah, once i fully used the compressed 0,0 in my code i went to full tc


import sys
sys.stdin = open('mirrors.in','r')
sys.stdout = open('mirrors.out','w')
sys.setrecursionlimit(2**30)
n,a,b = map(int,input().split())
mirrors = [input().split() for i in range(n)]
mirrors = [[int(i[0]),int(i[1]),i[2]] for i in mirrors]+[[a,b,'B']]+[[0,0,0]]

def compress():
    x,y = dict(),dict()
    for i in range(len(mirrors)):
        x[mirrors[i][0]] = x.get(mirrors[i][0],[])+[i]
        y[mirrors[i][1]] = y.get(mirrors[i][1],[])+[i]
    xkeys,ykeys = sorted(list(x.keys())),sorted(list(y.keys()))
    for i in range(len(x)):
        for j in x[xkeys[i]]:
            mirrors[j][0] = i
    for i in range(len(y)):
        for j in y[ykeys[i]]:
            mirrors[j][1] = i
compress()
startx,starty = mirrors[-1][0],mirrors[-1][1]
grid = [['.' for i in range(n+2)] for i in range(n+2)]
for i in mirrors:
    grid[i[1]][i[0]] = i[2]

log = set()
possible = False
dir = [[0,1],[1,0],[0,-1],[-1,0]] #R,U,L,D (y,x)
backslash = [3,2,1,0]
slash= [1,0,3,2]
ans = -1
def simulate(x,y,d,moves):
    global possible
    if len(log) != moves:
        return
    if 0 <= x < n+2 and 0 <= y < n+2:
        log.add((x,y,d))
        if grid[y][x] == 'B':
            possible = True
            return
        if grid[y][x] == '\\':
            d = backslash[d]
        if grid[y][x] == '/':
            d = slash[d]
        simulate(x+dir[d][1],y+dir[d][0],d,moves+1)

simulate(startx,starty,0,0)
if possible:
    ans = 0

if not possible:
    for i in range(n):
        log = set()
        if grid[mirrors[i][1]][mirrors[i][0]] == '\\':
            grid[mirrors[i][1]][mirrors[i][0]] = '/'
            simulate(startx,starty,0,0)
            grid[mirrors[i][1]][mirrors[i][0]] = '\\'

        if grid[mirrors[i][1]][mirrors[i][0]] == '/':
            grid[mirrors[i][1]][mirrors[i][0]] = '\\'
            simulate(startx,starty,0,0)
            grid[mirrors[i][1]][mirrors[i][0]] = '/'
        if possible:
            ans = i+1
            break

print(ans)