import sys
sys.stdin = open('mowing.in','r')
sys.stdout = open('mowing.out','w')
n = int(input())
dir = [input().split() for i in range(n)]
field = [[0 for i in range(2001)] for i in range(2001)]
coord = [1000,1000]
t= 0
x = []
for i in dir:
    for a in range(int(i[1])):
        t+=1
        if i[0] == 'N':
            coord[0]+=1
        if i[0] == 'E':
            coord[1]+=1
        if i[0] == 'S':
            coord[0]-=1
        if i[0] == 'W':
            coord[1]-=1
        if field[coord[0]][coord[1]] != 0:
            x.append(abs(field[coord[0]][coord[1]]-t))
        field[coord[0]][coord[1]] = t
if x == []:
    print(-1)
else:
    print(min(x))