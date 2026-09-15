import sys
sys.stdin = open('nocow.in','r')
sys.stdout = open('nocow.out','w')
n,k = map(int,input().split())
cows = [input().split()[4::] for i in range(n)]
cows = [i[0:len(i)-1] for i in cows]
nWordAdj = []
adjCount = len(cows[0])
for i in range(adjCount):
    adj = set()
    for j in range(n):
        adj.add(cows[j][i])
    nWordAdj.append(sorted(adj))

p = 1
for i in nWordAdj:
    p*=len(i)

def FindAdj(words):
    c = 0
    PreUpdateC = 0
    for i in words:
        dontHave= 0
        for j in cows:
            if j[currAdj] == i:
                dontHave+=1
        PreUpdateC = c
        c+=p-dontHave
        if c >= k:
            return (i,PreUpdateC)
ans = ''
for currAdj in range(adjCount):
    p = p//len(nWordAdj[currAdj])
    a = FindAdj(nWordAdj[currAdj])
    ans+=a[0]+' '
    nCows = []
    for i in cows:
        if i[currAdj] == a[0]:
            nCows.append(i)
    cows = nCows
    k-=a[1]
print(ans.strip())