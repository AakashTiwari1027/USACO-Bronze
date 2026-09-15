#nother 10 min problem that looked fun to do
#did this in 10mins while my vs code was bugging btw
#it didnt save the file after i ran it

import sys
sys.stdin = open('taming.in','r')
sys.stdout = open('taming.out','w')
n = int(input())
log = list(map(int,input().split()))
log[0] = 0

def complete(pos,val):
    if log[pos] != -1 and log[pos] != val:
        return False
    if log[pos] == val:
        return
    if log[pos] == -1:
        log[pos] = val
        complete(pos-1,val-1)
done = False
for i in range(n):
    if log[i] > 0:
        a = complete(i-1,log[i]-1)
        if a == False:
            done = True
            print(-1)
            break
if not done:
    print(log.count(0),log.count(0)+log.count(-1))
