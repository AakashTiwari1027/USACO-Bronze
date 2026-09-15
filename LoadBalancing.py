#complete search

import sys
sys.stdin = open('balancing.in','r')
sys.stdout = open('balancing.out','w')
n, b = map(int,input().split())
cows,x,y = [],[],[]
load = []
for i in range(n):
    cows.append(list(map(int,input().split())))
    x.append(cows[-1][0])
    y.append(cows[-1][1])
x = sorted(set(x))
y = sorted(set(y))
def check(a,b):
    q1,q2,q3,q4 = 0,0,0,0
    global cows
    for i in cows:
        if i[0]<a and i[1] > b:
            q1+=1
        if i[0] > a and i[1] > b:
            q2+=1
        if i[0] < a and i[1] < b:
            q3+=1
        if i[0] > a and i[1] <b:
            q4+=1
    return max(q1,q2,q3,q4)
for c in x:
    for d in y:
        e = c+1
        f = d+1
        load.append(check(e,f))
print(min(load))