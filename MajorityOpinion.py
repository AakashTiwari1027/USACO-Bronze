t = int(input())
out = []
for T in range(t):
    n = int(input())
    cows = list(map(int,input().split()))
    sol = set()
    if n < 3:
        if len(set(cows)) == 1:
            out.append([cows[0]])
        else:
            out.append([-1])
        continue
    a,b,c = cows[0],cows[1],cows[2]
    if a == b or a == c:
            sol.add(a)
    if b == c:
        sol.add(b)
    for i in range(3,n):
        if a == b or a == c:
            sol.add(a)
        if b == c:
            sol.add(b)
        a = b
        b = c
        c = cows[i]
    sol = sorted(list(sol))
    if len(sol) > 0:
        out.append(sol)
    else:
        out.append([-1])
for i in out:
    print(*i)