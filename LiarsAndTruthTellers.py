#we got the right idea which was representing as a graph with cows as vertex and claims as edges
#if claim is L then cows should be different colors, if claim is T then cows should be same colors
#we got that far
#coming to implementation, i did everything right but there was a bug that totally tanked us to 1 tc
#it was solved by making the graph edges biderectional
#which we could of yk, debugged and found that out
#or we could have randomly changed that (goated implemenation strategy: try random changes till it works OR delete+recode)
#still have tle on last four cases but not too worried about that


import sys
sys.stdin = open('truth.in','r')
sys.stdout = open('truth.out','w')
n,m = map(int,input().split())
edges = [input().split() for i in range(m)]

adj = [[] for i in range(n+1)]
visted = [False for i in range(n+1)]
possible = True
def dfs(node,color):
    global possible
    visted[node] = color
    for i in adj[node]:
        if visted[i[0]] == False:
            if i[1] == 'T':
                dfs(i[0],color)
            if i[1] == 'L':
                c = color
                if c == 'a':
                    c = 'b'
                else:
                    c = 'a'
                dfs(i[0],c)
        else:
            if i[1] == 'T' and visted[i[0]] != color:
                possible = False
                return
            if i[1] == 'L' and visted[i[0]] == color:
                possible = False
                return

for i in range(m):
    adj[int(edges[i][0])].append([int(edges[i][1]),edges[i][2]])
    adj[int(edges[i][1])].append([int(edges[i][0]),edges[i][2]])
    visted = [False]*(n+1)
    for j in range(1,n+1):
        if len(adj[j]) != 0 and visted[j] == False:
            dfs(j,'a')
    if not possible:
        print(i)
        break
if possible:
    print(m)