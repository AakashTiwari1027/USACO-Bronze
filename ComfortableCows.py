#you had to think about representing it in a 2d array, and make the observation that the only cows who could become
#comfortable or not are the added cow and the adjacent ones

n = int(input())
pasture = []
threes = 0
for i in range(1000):
    l = []
    for a in range(1000):
        l.append('E')
    pasture.append(l)
cows = []
c = []
for i in range(n):
    c.append(list(map(int,input().split())))
    cows.append(0)
for i in range(n):
    pasture[c[i][0]][c[i][1]] = i
    adj = [[c[i][0]+1,c[i][1]],[c[i][0]-1,c[i][1]],[c[i][0],c[i][1]-1],[c[i][0],c[i][1]+1]]
    count = 0
    for a in range(4):
        if adj[a][0] <= n and adj[a][0] >= 0:
            if adj[a][1] <= n and adj[a][1] >= 0:
                if pasture[adj[a][0]][adj[a][1]] != 'E':
                    if cows[pasture[adj[a][0]][adj[a][1]]] == 2:
                        threes+=1
                    if cows[pasture[adj[a][0]][adj[a][1]]] == 3:
                        threes-=1
                    cows[pasture[adj[a][0]][adj[a][1]]]+=1
                    count+=1
    a = cows[i]
    cows[i]+=count
    if a < 3 and cows[i] == 3:
        threes+=1
    if a <= 3 and cows[i] > 3:
        threes+=1
    print(threes)