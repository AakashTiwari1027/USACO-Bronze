import sys
sys.stdin = open('meeting.in','r')
sys.stdout = open('meeting.out','w')
n,m = map(int,input().split())
edges = [list(map(int,input().split())) for i in range(m)]
adj = [[] for i in range(n+1)]
for i in edges:
    adj[i[0]].append([i[1],i[2],i[3]])
bessie = set()
elsie = set()

def gen_all_paths(lst): #0,0,1
    l = []
    if lst == []:
        return
    for i in lst:
        if i[-1] == n:
            bessie.add(i[0])
            elsie.add(i[1])
        for j in adj[i[-1]]:
            a=i+[j[0]]
            a[0]+=j[1]
            a[1]+=j[2]
            l.append(a)
    gen_all_paths(l)

gen_all_paths([[0,0,1]])
ans = 'IMPOSSIBLE'
for i in bessie:
    for j in elsie:
        if i == j:
            if ans == "IMPOSSIBLE":
                ans = i
            elif i < ans:
                ans = i
print(ans)