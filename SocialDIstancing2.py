import sys
sys.stdin = open('socdist2.in','r')
sys.stdout = open('socdist2.out','w')
n = int(input())
cows = sorted([list(map(int,input().split())) for i in range(n)])

visted = [False for i in range(n+1)]
def simulate(curr,r):
    l = []
    if curr == []:
        return
    for i in curr:
        for j in range(n):
            if i == j:
                continue
            if visted[j] == False and abs(cows[i][0]-cows[j][0]) <= r:
                visted[j] = True
                l.append(j)
    simulate(l,r)
r= float('inf')
for i in range(n-1):
    if cows[i][1] != cows[i+1][1]:
        r = min(r,abs(cows[i][0]-cows[i+1][0])-1)
c = 0
for i in range(n):
    if cows[i][1] == 1 and visted[i] == False:
        simulate([i],r)
        c+=1
print(c)