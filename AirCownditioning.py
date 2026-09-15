#so
#sigma
#dude i had the right implementation, but it was horribly failing
#then i got the negative case (which i was thinking about earlier) via debugging, added two abs() and got full tc

n = int(input())
p = list(map(int,input().split()))
t = list(map(int,input().split()))
diff = [p[i]-t[i] for i in range(n)]+[0]

def subtract(a,b,c):
    for i in range(a,b+1):
        diff[i]-=c
curr = 0
t = 0
p = True

while p:
    while diff[curr] == 0:
        if curr+1 > n:
            p = False
            break
        curr+=1
    if diff[curr] < 0:
        m = diff[curr]
        for i in range(curr,n+1):
            if diff[i] >= 0:
                break
            m = max(m,diff[i])
        subtract(curr,i-1,m)
        t+=abs(m)
    if diff[curr] > 0:
        m = diff[curr]
        for i in range(curr,n+1):
            if diff[i] <= 0:
                break
            m = min(m,diff[i])
        subtract(curr,i-1,m)
        t+=abs(m)
print(t)