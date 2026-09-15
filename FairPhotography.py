import sys
sys.stdin = open('fairphoto.in','r')
sys.stdout = open('fairphoto.out','w')
n = int(input())
cows = [input().split() for i in range(n)]
cows = sorted([[int(i[0]),i[1]] for i in cows])

pre = []
dic = {}
for i in cows:
    if i[1] == 'G':
        pre.append(1)
    else:
        pre.append(-1)
for i in range(1,n):
    pre[i]+=pre[i-1]

for i in range(n):
    dic[pre[i]] = dic.get(pre[i],[])+[i]
cows.append(cows[-1])
ans = []
for i in dic.values():
    ans.append(cows[i[-1]][0]-cows[i[0]+1][0])

a =0
for i in range(n):
    if cows[i][1] !=  cows[i+1][1]:
        ans.append(cows[i][0]-cows[a][0])
        a = i+1
        continue

print(max(ans))