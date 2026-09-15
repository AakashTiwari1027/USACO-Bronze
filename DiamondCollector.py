import sys
sys.stdin = open('diamond.in','r')
sys.stdout = open('diamond.out','w')
n,k = map(int,input().split())
diamonds = [int(input()) for i in range(n)]
totals = []
diamonds.append(10000000)
diamonds.sort()
for a in range(n):
    c = 0
    for b in range(a,n):
        if diamonds[b]-diamonds[a] > k:
            totals.append(c)
            break
        if diamonds[b]-diamonds[a] <= k:
            c+=1

print(max(totals))