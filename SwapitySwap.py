#My main idea was just to figure out when the list cycled back by figuring out when each index of the list cycled back, and find
#the lcm of all of the indexs time to cycle back
#implementation prob was me using // instead of % lol

import sys
from math import gcd
sys.stdin = open('swap.in','r')
sys.stdout = open('swap.out','w')
n,k = map(int,input().split())
cows= [i+1 for i in range(n)]
a = list(map(int,input().split()))
b = list(map(int,input().split()))
cycle = []
journey = []
count = []
def swap(rep):
    global cows
    global a
    global b
    for i in range(rep):
        cows[a[0]-1:a[1]] = reversed(cows[a[0]-1:a[1]])
        cows[b[0]-1:b[1]] = reversed(cows[b[0]-1:b[1]])
    return cows
swap(1)
for i in range(1,n+1):
    cycle.append([i-1,cows.index(i)])
def Cycle(a):
    global cycle
    global journey
    journey.append(cycle[a][0])
    if journey[-1] == journey[0] and len(journey) > 1:
        count.append(len(journey)-1)
        return
    Cycle(cycle[a][1])
for i in range(n):
    Cycle(i)
    journey = []
lcm = 1
for i in count:
    lcm = lcm*i//gcd(lcm,i)
if lcm > k:
    l = (swap(k-1))
    for i in l:
        print(i)
else:
    l = (swap((k%lcm)-1))
    for i in l:
        print(i)