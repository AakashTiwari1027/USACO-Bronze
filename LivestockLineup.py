import sys
from itertools import permutations
sys.stdin = open('lineup.in','r')
sys.stdout = open('lineup.out','w')
n = int(input())
cons = [input().split() for i in range(n)]
cows = ['Bessie', 'Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy', 'Sue']
p = list(permutations(cows))
ans = []
for i in p:
    i = list(i)
    count = 0
    for c in cons:
        if abs(i.index(c[0])-i.index(c[-1])) == 1:
            count+=1
    if count == n:
        ans.append(i)
for i in (min(ans)):
    print(i)