import sys
sys.stdin = open('cbarn.in','r')
sys.stdout = open('cbarn.out','w')
n = int(input())
r = [int(input()) for i in range(n)]
counts= []
for i in range(n):
    r.append(r.pop(0))
    c = 0
    for j in range(n):
        c+=r[j]*j
    counts.append(c)

print(min(counts))