#make the observation that h index can only be upped by one

n,l = map(int,input().split())
c = sorted(list(map(int,input().split())),reverse=True)
hi = 0
for i in range(n):
    if c[i] >= i+1:
        hi = i+1
    if c[i]+1 == i+1 and l > 0:
        hi = i+1
        l-=1

print(hi)

