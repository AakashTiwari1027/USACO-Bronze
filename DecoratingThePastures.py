#our normal bipartate implementation assumes the graph is fully connected, which in this problem it wasnt!
#so we had to do a bipartate check on every component of the graph

import sys
sys.setrecursionlimit(2**30)
sys.stdin = open('decorate.in','r')
sys.stdout = open('decorate.out','w')
n,m = map(int,input().split())
edges = [list(map(int,input().split())) for i in range(m)]
adj = [[] for i in range(m+1)]

for i in edges:
    adj[i[0]].append(i[1])
    adj[i[1]].append(i[0])

visted= [False for i in range(n+1)]
possible = True
numF,numJ = 0,0
def bipartate(node,color):
    global possible
    global numF
    global numJ
    if color == 'F':
        numF+=1
    if color == 'J':
        numJ+=1
    visted[node] = color
    for i in adj[node]:
        flipColor = color
        if flipColor == 'F':
            flipColor = 'J'
        elif flipColor == 'J':
            flipColor = 'F'

        if visted[i] == False:
            bipartate(i,flipColor)
        else:
            if visted[i] == color:
                possible = False
ans = 0
for i in range(1,n+1):
    if visted[i] == False:
        numF,numJ = 0,0
        bipartate(i,'F')
        if possible:
            ans+=max(numF,numJ)
if not possible:
    print(-1)
else:
    print(ans)