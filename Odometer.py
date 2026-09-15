#With the beauty of deleting everything and recoding, this problem was solved, and so much frustration dissapeared

import sys
sys.stdin = open('odometer.in','r')
sys.stdout = open('odometer.out','w')
x,y = map(int,input().split())
intresting = []

for i in range(3,18):
    for d in range(10):
        base = str(d)*i
        for j in range(i):
            for k in range(10):
                l = list(base)
                l[j] = str(k)
                intresting.append(''.join(l))
intr = []
for i in intresting:
    if i[0] != '0' and len(set(i)) == 2:
        intr.append(i)
c = 0
for i in intr:
    if x <= int(i) <= y:
        c+=1


print(c)
