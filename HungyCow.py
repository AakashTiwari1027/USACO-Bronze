#tbh the only reason i didnt get without sol is cuz the observation is really weird
#i didnt think to realize that the amount eaten is the total-remaining

n,t = map(int,input().split())
d = [list(map(int,input().split())) for i in range(n)]
d.append([t+1,0])
total,remain,last = 0,0,0
for i in range(n+1):
    total+=d[i][1]
    remain-=d[i][0]-last
    last = d[i][0]
    remain = max(0,remain)
    remain+=d[i][1]
print(total-remain)