import sys
sys.stdin = open('milkorder.in','r')
sys.stdout = open('milkorder.out','w')
n,m,k = map(int,input().split())
relPos = list(map(int,input().split()))
cows = [-1 for i in range(n)]
for i in range(k):
    a,b = map(int,input().split())
    cows[b-1] =a

for i in range(n):
    if cows[i] == -1:
        pcows = list(cows)
        pcows[i] = 1
        ind = 0
        j = 0
        while ind < n and j < m:
            if relPos[j] in pcows:
                ind = pcows.index(relPos[j])
                j+=1
            if pcows[ind] in relPos:
                if relPos.index(pcows[ind]) > j:
                    break
            else:
                if pcows[ind] == -1:
                    pcows[ind] = relPos[j]
                    j+=1
            ind+=1
        if j == m:
            print(i+1)
            break


