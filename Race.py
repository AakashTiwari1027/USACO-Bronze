#just spent an hour trying to make this faster, but it was just a python prob
#but yeah this was the right solution, learned it from alphastar

import sys
from math import ceil
sys.stdin = open('race.in','r')
sys.stdout = open('race.out','w')
k,n = map(int,input().split())
x = [int(input()) for i in range(n)]

def solve(x):
    dist,time = 0,0
    speed = 0
    while dist < k:
        speed+=1
        if speed < x:
            if dist+speed <= k:
                dist+=speed
                time+=1
            else:
                break
        if speed >= x:
            if dist+2*speed <= k:
                dist+=2*speed
                time+=2
            else:
                break
    return time+ceil((k-dist)/speed)
for i in x:
    print(solve(i))