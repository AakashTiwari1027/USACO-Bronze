#honestly i neg diffed this problem with recursion
#took a bit of time cuz the problem said 'perfectly balanced' strings instead of balanced

import sys
sys.stdin = open('hshoe.in','r')
sys.stdout = open('hshoe.out','w')
n = int(input())
grid = [input() for i in range(n)]
ans = 0
visted= [[False for i in range(n)] for i in range(n)]
def path(x,y,s,l):
    global ans
    if l%2 == 0:
        if s == '('*(l//2)+')'*(l//2):
            ans = max(ans,l)
    dir = [[0,1],[0,-1],[1,0],[-1,0]]
    alpha = 'DURL'
    for i in dir:
        if 0 <= x+i[0] < n and 0 <= y+i[1] < n:
            if visted[y+i[1]][x+i[0]] == False:
                visted[y+i[1]][x+i[0]] = True
                path(x+i[0],y+i[1],s+grid[y+i[1]][x+i[0]],l+1)
                visted[y+i[1]][x+i[0]] = False
visted[0][0] = True
path(0,0,grid[0][0],1)
print(ans)