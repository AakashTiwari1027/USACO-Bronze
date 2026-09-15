from math import floor

t= int(input())
out = []
for T in range(t):
    n = int(input())
    h = list(map(int,input().split()))
    a = list(map(int,input().split()))
    t = list(map(int,input().split()))
    plants = [[t[i],h[i],a[i]] for i in range(n)]
    plants.sort()
    lb,ub= 0,10000000000000000
    p = True
    for i in range(n-1):
        if plants[i+1][2] == plants[i][2]:
            if plants[i][1] > plants[i+1][1]:
                continue
            else:
                p = False
                break
        inter = (plants[i][1]-plants[i+1][1])/(plants[i+1][2]-plants[i][2])
        if plants[i][1] > plants[i+1][1] and inter > 0:
            ub = min(floor(inter)+1,ub)
        else:
            lb = max(floor(inter)+1,lb)
    if p and lb < ub:
        out.append(lb)
    else:
        out.append(-1)
for i in out:
    print(i)