#good problem
#review this, youll remember the solution it was pretty nice, but hard to explain

import sys
sys.stdin = open('scramble.in','r')
sys.stdout = open('scramble.out','w')
n = int(input())
names = [input() for i in range(n)]
high = sorted([[''.join(sorted(names[i])),i,False] for i in range(n)])
low = sorted([[''.join(sorted(names[i],reverse=True)),i,True] for i in range(n)])
out = [[] for i in range(n)]

lst = sorted(high+low)
s,r = 0 ,0

for i in range(len(lst)):
    if lst[i][2] == False:
        out[lst[i][1]].append(i-s)
        s+=1
    else:
        out[lst[i][1]].append(i-r-1)
        r+=1
for i in out:
    print(i[0]+1,i[1]+1)