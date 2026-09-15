#i debugged really nicely on this one i feel

n,m = map(int,input().split())
field = [input() for i in range(n)]
partners = set()
count = 0
for y in range(n):
    for x in range(m):
        if field[y][x] != 'G':
            continue
        a = [[0,1],[1,0],[0,-1],[-1,0]]
        adj = []
        for i in a:
            if 0 <= y+i[0] < n and 0 <= x+i[1] < m:
                if field[y+i[0]][x+i[1]] == 'C':
                    adj.append(i)
        if len(adj) >= 3:
            count+=1
        if len(adj) == 2:
            partners.add((y+adj[0][0],x+adj[0][1],y+adj[1][0],x+adj[1][1]))
            partners.add((y+adj[1][0],x+adj[1][1],y+adj[0][0],x+adj[0][1]))
    
print(count+len(partners)//2)
