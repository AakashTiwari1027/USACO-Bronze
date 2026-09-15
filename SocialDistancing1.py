import sys
#sys.stdin = open('socdist1.in','r')
#sys.stdout = open('socdist1.out','w')
n = int(input())
cows = input()
c = 0
gaps = []
for i in range(n):
    if cows[i] == '1':
        if c > 0:
            gaps.append(c)
        c = 0
    if cows[i] == '0':
        c+=1

print(gaps)
gaps = sorted(gaps,reverse=True)
d= min(gaps)
count = 0
for i in gaps:
    if i == (2*d)-1:
        count+=1
    if i == (3*d)-1:
        count=2
if count == 2:
    print(d+1)
else:
    print(d)