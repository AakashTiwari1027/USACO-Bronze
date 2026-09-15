#really nice application of recursion into a bronze problem

import sys
sys.stdin = open('hopscotch.in','r')
sys.stdout = open('hopscotch.out','w')
r,c = map(int,input().split())
board = [input() for i in range(r)]

ans = 0
def recurse(x,y,color):
    global ans
    if x == c-1 and y == r-1:
        ans+=1
        return
    for i in range(y+1,r):
        for j in range(x+1,c):
            if board[i][j] != color:
                recurse(j,i,board[i][j])

recurse(0,0,board[0][0])
print(ans)