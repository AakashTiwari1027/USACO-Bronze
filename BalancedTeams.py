import sys
from itertools import combinations
sys.stdin = open('bteams.in','r')
sys.stdout = open('bteams.out','w')
cows = [int(input()) for i in range(12)]
s = sum(cows)
teams = (list(combinations(cows,3)))
ans = []
for i in range(220):
    for j in range(i+1,220):
        if len(set(teams[i]+teams[j])) != 6:
            continue
        for k in range(j+1,220):
            if len(set(teams[i]+teams[j]+teams[k])) != 9:
                continue
            a = sum(teams[i])
            b = sum(teams[j])
            c = sum(teams[k])
            ans.append(max(a,b,c,s-(a+b+c))-min(a,b,c,s-(a+b+c)))


print(min(ans))