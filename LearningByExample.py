import sys
from math import ceil
sys.stdin = open('learning.in','r')
sys.stdout = open('learning.out','w')
n,a,b = map(int,input().split())
cows = [[0,'NS'],[1000000001,'NS']]
for i in range(n):
    inp = input().split()
    cows.append([int(inp[1]),inp[0]])
cows.sort()
ans = 0
for i in range(1,n+1):
    if cows[i][1] == 'S':
        lclaimed = ceil((cows[i][0]-cows[i-1][0]+1)/2)
        lbound = cows[i][0]-lclaimed+1
        rclaimed = ceil((cows[i+1][0]-cows[i][0]+1)/2)
        rbound = cows[i][0]+rclaimed-1
        overlap = min(rbound,b)-max(lbound,a)+1
        ans+=(max(overlap,0))
oddAdjS = 0
for i in range(1,n+1):
    if cows[i][1] == 'S' and cows[i+1][1] == 'S':
        if (cows[i+1][0]-cows[i][0]+1)%2 == 1 and a <= (cows[i+1][0]+cows[i][0])/2 <= b:
            oddAdjS+=1
print(ans-oddAdjS)
