#our first approach, which we got pretty instantly from just thinking was, scan from left to right, and for every W add the amount of c's seen times amout of o's seen
#this didnt work for cases like CCOCW
#bridging off of this edge case, we find the amout of distinct CO pairings, and now for every W add the amout of CO pairings
#pretty good problem solving prob

import sys
sys.stdin = open('cow.in','r')
sys.stdout = open('cow.out','w')
n = int(input())
s = input()
c = 0
co = 0
ans = 0
for i in s:
    if i == 'C':
        c+=1
    if i == 'O':
        co+=c
    if i == 'W':
        ans+=co
print(ans)