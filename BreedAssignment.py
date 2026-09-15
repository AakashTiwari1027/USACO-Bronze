#okayyyy
#recursion prob, but like from 5 on testcases tle
#so, instead of checking for validity after filling everything out, check it on the way and prune incorrect cases early
#yeah that was about it for this problem
#i tried doing that, but had to look at sol a bit
#basically we only assign a breed if it doenst conflict with earlier assigned breeds
#also had to reset breed[curr] back to 0 after assigning, figured that out with rand strat

import sys
sys.stdin = open('assign.in','r')
sys.stdout = open('assign.out','w')
n,k = map(int,input().split())
rel = [input().split() for i in range(k)]
rel = [[i[0],int(i[1]),int(i[2])] for i in rel]
breed = [0 for i in range(n)]
ans = 0

def generate(curr):
    global ans
    if curr == n:
        ans+=1
        return
    for i in range(1,4):
        works = True
        for r in rel:
            other = -1
            if r[1]-1 == curr:
                other = r[2]
            if r[2]-1 == curr:
                other = r[1]
            if breed[other-1] == 0:
                continue
            if other != -1:
                if r[0] == 'S':
                    if i != breed[other-1]:
                        works = False
                        break
                if r[0] == 'D':
                    if i == breed[other-1]:
                        works = False
                        break
        if works:
            breed[curr] = i
            generate(curr+1)
        breed[curr] = 0

generate(0)
print(ans)