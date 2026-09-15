import time
n = int(input())
s = time.time()
x,y = [],[]
for i in range(n):
    inp = list(map(int,input().split()))
    x.append(inp[0])
    y.append(inp[1])
ans = 0
xlen,ylen = len(set(x)),len(set(y))
if xlen == 3 or ylen == 3:
    ans = 1

yDict = dict()
for i in set(y):
    yDict[i] = set()
for i in range(n):
    yDict[y[i]].add(x[i])
maxRemove = 0
for i in yDict.values():
    maxRemove = max(maxRemove,len(i))
if xlen-maxRemove <= 2:
    ans = 1
print(yDict,xlen)

xDict = dict()
for i in set(x):
    xDict[i] = set()
for i in range(n):
    xDict[x[i]].add(y[i])
maxRemove = 0
for i in xDict.values():
    maxRemove = max(maxRemove,len(i))
if ylen-maxRemove <= 2:
    ans = 1
e = time.time()
print(ans)
