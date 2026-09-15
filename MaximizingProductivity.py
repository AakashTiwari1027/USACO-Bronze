n,q = map(int,input().split())
c,t = list(map(int,input().split())),list(map(int,input().split()))
query = [list(map(int,input().split())) for i in range(q)]
d = [c[i]-t[i] for i in range(n)]
d=sorted(d,reverse=True)
for i in query:
    if d[i[0]-1] > i[1]:
        print('YES')
    else:
        print('NO')