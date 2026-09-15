import sys
sys.stdin = open('evolution.in','r')
sys.stdout = open('evolution.out','w')
n = int(input())
cows = [input().split() for i in range(n)]
for i in range(n):
    cows[i][0] = int(cows[i][0])
works = True
for a in range(n):
    for b in range(a+1,n):
        for c in range(b+1,n):
            if len(set(cows[a][1::]+cows[b][1::])) < cows[a][0]+cows[b][0] and len(set(cows[c][1::]+cows[b][1::])) < cows[c][0]+cows[b][0] and len(set(cows[a][1::]+cows[c][1::])) == cows[a][0]+cows[c][0]:
                works = False
if works:
    print('yes')
else:
    print('no')