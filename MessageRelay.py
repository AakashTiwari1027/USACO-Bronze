#pretty easy problem with graphs, i had and optimization that i dont think i even really needed which was if you dont send to a 0, your loopy


import sys
sys.setrecursionlimit(2000)
sys.stdin = open('relay.in','r')
sys.stdout = open('relay.out','w')
n = int(input())
adj = [int(input()) for i in range(n)]
visted= [False]*n
loopy = True

def dfs(node):
    global loopy
    visted[node] = True
    if adj[node] == 0:
        loopy = False
    else:
        if visted[adj[node]-1] == False:
            dfs(adj[node]-1)
count = 0

for i in range(n):
    loopy = True
    visted = [False]*n
    dfs(i)
    if loopy == False:
        count+=1

print(count)