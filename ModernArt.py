#You just want to check colors that arent rectangles, if so than see which colors are overlapping if it was a rectangle, and those
#are the colors that came later

import sys
sys.stdin = open('art.in','r')
sys.stdout = open('art.out','w')
n = int(input())
canvas = [input() for i in range(n)]
colors = set()
order = []
count = 0
for i in range(n):
    for a in range(n):
        if canvas[i][a] != '0':
            colors.add(canvas[i][a])
colors = list(colors)
rect = []
for i in colors:
    x,y = [],[]
    for a in range(n):
        for b in range(n):
            if canvas[a][b] == i:
                x.append(b)
                y.append(a)
    rect.append([min(x),max(x),min(y),max(y)])

for i in range(len(colors)):
    for a in range(rect[i][2],rect[i][3]+1):
        for b in range(rect[i][0],rect[i][1]+1):
            if canvas[a][b] != colors[i]:
                order.append([colors[i],canvas[a][b]])
for i in colors:
    c = 0
    C = 0
    for a in order:
        if a[0] == i:
           c+=1
        if a[1] == i:
            C+=1
            break
    if C == 0:
        count+=1
print(count)