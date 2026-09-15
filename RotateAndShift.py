n,k,t = map(int,input().split())
a = list(map(int,input().split()))

def sim():
    global init
    l = [init[i] for i in a]
    l.insert(0,l[k-1])
    l.pop(k)
    for i in range(k):
        init[a[i]] = l[i]
init = [i for i in range(n)]

d = []
m = [i for i in range(n)]
for i in range(k):
    if i == k-1:
        l=[n-(a[i]-a[0])]*(n-(a[i]-a[0]))
    else:
        l = [a[i+1]-a[i]]*(a[i+1]-a[i])
    d+=l
for i in range(k):
    if i == k-1:
        ind = a[0]
    else:
        ind = a[i+1]
    m[a[i]] = ind
final = [0 for i in range(n)]
print(d,m)
for i in range(n):
    final[(m[i]+(t-d[i]))%n] = i

print(final)