#pretty simple simulation problem, you have to make the observation that we cant get stuck in a cycle for full testcases though

import sys
sys.stdin = open('mirror.in','r')
sys.stdout = open('mirror.out','w')
sys.setrecursionlimit(2**30)
n,m = map(int,input().split())
field = [input() for i in range(n)]

dir = [[0,1],[1,0],[0,-1],[-1,0]] #y,x RDLU
backslash = [1,0,3,2] #\
slash = [3,2,1,0] 

count = 0
def reflect(x,y,d):
    global count
    if 0 <= x < m and 0 <= y < n:
        count+=1
        if field[y][x] == '\\':
            newD = backslash[d]
        if field[y][x] == '/':
            newD = slash[d]
        reflect(x+dir[newD][1],y+dir[newD][0],newD)
ans = []
for i in range(n):
    count =0
    reflect(0,i,0)
    ans.append(count)
    count = 0
    reflect(m-1,i,2)
    ans.append(count)
for i in range(m):
    count = 0
    reflect(i,0,1)
    ans.append(count)
    count = 0
    reflect(i,n-1,3)
    ans.append(count)
print(max(ans))