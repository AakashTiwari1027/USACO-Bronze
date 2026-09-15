import sys
sys.stdin = open('milktemp.in','r')
sys.stdout = open('milktemp.out','w')
n,x,y,z = map(int,input().split())
cows = [list(map(int,input().split())) for i in range(n)]
s,e = y-x,z-y
sort = []
for i in cows:
    sort.append([i[0],'E'])
    sort.append([i[1],'S'])
sort.sort()
milk = n*x
ans = [milk]
for i in sort:
    if i[1] == 'E':
        milk+=s
    if i[1] == 'S':
        milk+=e
    ans.append(milk)

print(max(ans))