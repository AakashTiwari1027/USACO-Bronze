import sys
sys.stdin = open('lazy.in','r')
sys.stdout = open('lazy.out','w')
n,k = map(int,input().split())
grass = [list(map(int,input().split())) for i in range(n)]

field = [0 for i in range(1000000)]
for i in grass:
    field[i[1]] = i[0]
counts = []
s,e = 0,min((2*k)+1,len(field))
g = sum(field[s:e])
counts.append(g)
for i in range(len(field)-e):
    g-=field[s]
    g+=field[e]
    s+=1
    e+=1
    counts.append(g)
counts = [i for i in counts if i != 0]
print(max(counts))