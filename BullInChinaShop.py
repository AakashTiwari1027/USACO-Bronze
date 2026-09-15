#So. Sigma.
#dude i couldnt even wrap my mind around this problem when i was doing bronze practice and i just did it first try
#i couldnt visualize it very well, what i changed this time was instead of laying the parts side by side, i put the parts on the same nxn grid
#now it was alot easier to visualize how to move the parts around, and from the small bounds i knew i just had to simply complete search on it
#and idk after that i just did it, and i think i implemented it pretty well

import sys
sys.stdin = open('bcs.in','r')
sys.stdout = open('bcs.out','w')
n,k = map(int,input().split())
og = [list(input()) for i in range(n)]
parts = [[input() for i in range(n)] for j in range(k)]

def move(grid,x,y):
    copy = [['.' for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '#':
                if 0 <= i+y < n and 0 <= j+x < n:
                    copy[i+y][j+x] = '#'
                else:
                    return False
    return copy

def join(a,b):
    joined = [['.' for i in range(n)] for j in range(n)]
    for y in range(n):
        for x in range(n):
            if a[y][x] == '#' and b[y][x] == '#':
                return False
            if a[y][x] == '#':
                joined[y][x] = '#'
            if b[y][x] == '#':
                joined[y][x] = '#'
    return joined


for p1 in range(k):
    for p2 in range(p1+1,k):
            for y1 in range(-n,n):
                for x1 in range(-n,n):
                    a = move(parts[p1],x1,y1)
                    if a != False:
                        for y2 in range(-n,n):
                            for x2 in range(-n,n):
                                b = move(parts[p2],x2,y2)
                                if b != False:
                                    res = join(a,b)
                                    if res != False and res == og:
                                        print(p1+1,p2+1)
                                        break