#pretty simple once you realize that the cow you are going to remove is either maxx,maxy,minx,miny since those are on the border of our rectangle
#still can be done more effecient i think, i dont like the fact that we are recomputing area when we already sorted x and y

import sys
sys.stdin = open('reduce.in','r')
sys.stdout = open('reduce.out','w')
n = int(input())
cows= [list(map(int,input().split())) for i in range(n)]
x,y = sorted([[cows[i][0],i] for i in range(n)]),sorted([[cows[i][1],i] for i in range(n)])
def calc_area(lst):
    minx,miny,maxx,maxy = 10000000,100000000,0,0
    for i in lst:
        minx = min(minx,i[0])
        miny = min(miny,i[1])
        maxx = max(maxx,i[0])
        maxy = max(maxy,i[1])
    return (maxx-minx)*(maxy-miny)
a,b,c,d = list(cows),list(cows),list(cows),list(cows)
a.pop(x[0][1])
b.pop(x[-1][1])
c.pop(y[0][1])
d.pop(y[-1][1])
print(min(calc_area(a),calc_area(b),calc_area(c),calc_area(d)))