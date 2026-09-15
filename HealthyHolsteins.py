'''
ID: aakasht3
LANG: PYTHON3
TASK: holstein
'''
import sys
sys.stdin = open('holstein.in','r')
sys.stdout = open('holstein.out','w')
v = int(input())
vit =  list(map(int,input().split()))
g = int(input())
feeds = [list(map(int,input().split())) for i in range(g)]
p = []
def generateAllBinaryStrings(n, arr, i): 
    global p
    if i == n:
        p.append(list(arr))
        return
    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1) 
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1) 
arr = [None]*g
generateAllBinaryStrings(g,arr,0)
p = p[1::]
ans =[ ]
for i in p:
    c = [0]*v
    works = True
    for a in range(g):
        if i[a] == 1:
            for b in range(v):
                c[b]+=feeds[a][b]
    for V in range(v):
        if c[V] < vit[V]:
            works = False
    if works:
        l = []
        for d in range(g):
            if i[d] == 1:
                l.append(feeds[d])
        ans.append(l)
lens = [len(i) for i in ans]
a = []
for i in range(len(ans)):
    if lens[i] == min(lens):
        a.append(ans[i])
ans =a
print(len(min(ans)),*sorted([feeds.index(i)+1 for i in min(ans)]))


