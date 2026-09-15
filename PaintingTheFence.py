import sys
sys.stdin = open('paint.in','r')
sys.stdout = open('paint.out','w')
n = int(input())
moves = [input().split() for i in range(n)]
coords = []
curr = 0
for i in moves:
    if i[1] == 'R':
        coords.append([curr,True])
        curr+=int(i[0])
        coords.append([curr,False])
    if i[1] == "L":
        coords.append([curr,False])
        curr-=int(i[0])
        coords.append([curr,True])
coords.sort()
layers = 1
c = 0
for i in range(1,len(coords)):
    if layers >= 2:
        c+=(abs(coords[i-1][0]-coords[i][0]))
    if coords[i][1] == True:
        layers+=1
    if coords[i][1] == False:
        layers-=1
print(c)