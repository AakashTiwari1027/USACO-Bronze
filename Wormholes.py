import sys
sys.stdin = open('wormhole.in','r')
sys.stdout = open('wormhole.out','w')
n = int(input())
cows = [list(map(int,input().split())) for i in range(n)]
cows.sort()
ydict = {}
for i in range(n):
    ydict[cows[i][1]] = ydict.get(cows[i][1],[])+[[cows[i][0],i]]

partner = [-1 for i in range(n)]
pairings = []
def gen_pairings(curr):
    if curr == n:
        pairings.append(list(partner))
        return
    if partner[curr] != -1:
        gen_pairings(curr+1)
    for i in range(n):
        if i != curr and partner[i] == -1 and partner[curr] == -1:
            partner[curr] = i
            partner[i] = curr
            gen_pairings(curr+1)
            partner[curr] = -1
            partner[i] = -1
gen_pairings(0)

def cycle(portal,pairing):
    visted = [False for i in range(n)]
    while True:
        if visted[portal] == True:
            return True
        visted[portal] = True
        portal = pairing[portal]
        y = cows[portal][1]
        x = cows[portal][0]
        no_further = True
        for i in range(1,len(ydict[y])):
            if ydict[y][i-1][0] == x:
                portal = ydict[y][i][1]
                no_further = False
                break
        if no_further:
            return False

ans = 0
for i in pairings:
    for j in range(n):
        if cycle(j,i):
            ans+=1
            break

print(ans)