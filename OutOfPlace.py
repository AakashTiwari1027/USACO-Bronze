import sys
sys.stdin = open('outofplace.in','r')
sys.stdout = open('outofplace.out','w')
n = int(input())
cows = [int(input()) for i in range(n)]
sort = sorted(cows)
swaps = -1
for i in range(n):
    if cows[i] != sort[i]:
        swaps+=1
print(max(swaps,0))

