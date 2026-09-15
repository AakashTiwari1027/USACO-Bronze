n = int(input())
b = [int(input()) for i in range(n)]
p = []
def solve(c):
    global b
    s = set()
    for i in range(c,n):
        s.add(b[i])
        if len(s) > 2:
            s.remove(b[i])
            break
    if len(s) > 1:
        return max(b[c:i].count(list(s)[0]),b[c:i].count(list(s)[1]))
for i in range(n-1):
    p.append(solve(i))

p = [i for i in p if i != None]
print(max(p))
