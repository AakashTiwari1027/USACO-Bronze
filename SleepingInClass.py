#good prob, basicly the list has to be combined into a factor of the sum of the list, check if those facotrs are possible

out = []
t = int(input())
for x in range(t):
    n = int(input())
    log = list(map(int,input().split()))
    if len(set(log)) == 1:
        out.append(0)
        break
    total = sum(log)
    factors = []
    for i in range(1,n//2+1):
        if total == 0:
            break
        if total%i == 0:
            factors.append(i)
            factors.append(int(total/i))
    factors = sorted(factors,reverse = True)
    for f in factors:
        count = 0
        c = 0
        for i in range(n):
            c+=log[i]
            if c == total/f:
                count+=1
                c = 0
        if count == f:
            out.append(n-f)
            break
for i in out:
    print(i)