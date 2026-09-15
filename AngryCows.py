#tried to do it dfs, but problem specified that all cows blow up simultaniously
#didnt think that matter, but i recoded anyway and got full tc

import sys
sys.stdin = open('angry.in','r')
sys.stdout = open('angry.out','w')
n = int(input())
hay = sorted([int(input()) for i in range(n)])
visted = [False for i in range(n)]
hit = 0
ans = 0

def boom(l,pow):
    global hit
    global ans
    if l == []:
        return
    for i in l:
        visted[i] = True
    lst = []
    for i in l:
        for j in range(n):
            if visted[j] == False and abs(hay[i]-hay[j]) <= pow:
                visted[j] = True
                hit+=1
                lst.append(j)
    ans = max(ans,hit)
    boom(lst,pow+1)

for i in range(n):
    visted = [False]*n
    hit = 0
    boom([i],1)
print(ans+1)