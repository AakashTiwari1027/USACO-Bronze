#a strat i could have done to get the sol to this problem was look at similarities in the solved outputs
#which was that they were that the diff between min and max was 17

import sys
sys.stdin = open('skidesign.in','r')
sys.stdout = open('skidesign.out','w')
n = int(input())
hills = [int(input()) for i in range(n)]
a,b = -1,16
costs = []
for i in range(83):
    a+=1
    b+=1
    cost = 0
    for h in hills:
        if h < a:
            cost+=(a-h)**2
        if h > b:
            cost+=(h-b)**2
    costs.append(cost)

print(min(costs))