import sys
sys.stdin = open('reorder.in','r')
sys.stdout = open('reorder.out','w')
n = int(input())
a,b = [int(input()) for i in range(n)],[int(input()) for i in range(n)]
c= [0 for i in range(n)]

count = 0
totalCount = 0
sames = [i for i in range(n) if a[i]==b[i]]

def cycle(val):
    global c
    global count
    n2 = b.index(val)
    n3 = a[n2]

    if n3 == c[0] or c[n2] != 0:
        return
    c[n2] = val
    count+=1
    cycle(n3)

counts = []
while 0 in c:
    count = 0
    cycle(a[c.index(0)])
    counts.append(count)
    totalCount+=1
totalCount-=len(sames)
if a == b:
    print(0,-1)
else:
    print(totalCount,max(counts))

#SOl 1