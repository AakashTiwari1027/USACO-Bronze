n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ind = [-1 for i in range(n+1)]
for i in range(n):
    ind[a[i]] = i
ans = 0

for i in range(n):
    if a[i] != b[i]:
        a.remove(b[i])
        a.insert(i,b[i])
        ans+=1
print(ans)