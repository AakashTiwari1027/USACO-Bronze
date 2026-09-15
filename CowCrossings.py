#who the goat? who the goat?
#IM THE GOAT
#kamal hai yaar
#this felt like a really easy problem that i should have been able to solve, but i got wrong
#but im just so cracked that i debugged, found the issue and got full tc

import sys
sys.stdin = open('crossings.in','r')
sys.stdout = open('crossings.out','w')
n = int(input())
cows = [list(map(int,input().split())) for i in range(n)]
x,y = sorted([i[0] for i in cows]),sorted([i[1] for i in cows])
cowsDict = {i[0]:i[1] for i in cows}
ans = 0
visted = [False for i in range(n)]
latestCow = -float('inf')
for i in range(n):
    if cowsDict[x[i]] < latestCow:
        ans+=1
        visted[i] = True
    if cowsDict[x[i]] > latestCow:
        latestCow = cowsDict[x[i]]
earliestCow = float('inf')
for i in reversed(range(n)):
    if cowsDict[x[i]] < earliestCow:
        earliestCow = cowsDict[x[i]]
    if cowsDict[x[i]] > earliestCow:
        if visted[i] == False:
            ans+=1

def bruteForce():
    ans = 0
    for i in cows:
        for j in cows:
            if i == j:
                continue
            if i[0] < j[0] and i[1] > j[1]:
                ans+=1
                break
            if i[0] > j[0] and i[1] < j[1]:
                ans+=1
                break
    return n-ans
print(n-ans)