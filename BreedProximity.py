#bit of a different approach to slidin windows

import sys
sys.stdin = open('proximity.in','r')
sys.stdout = open('proximity.out','w')
n,k = map(int,input().split())
lst = [int(input()) for i in range(n)]
breeds = [0 for i in range(max(lst)+1)]
conflicts = [-1]
for i in range(k+1):
    breeds[lst[i]]+=1
    if breeds[lst[i]] > 1:
        conflicts.append(lst[i])
s,e = 0,k+1
for i in range(k+1,n):
    breeds[lst[s]]-=1
    breeds[lst[i]]+=1
    if breeds[lst[i]] > 1:
        conflicts.append(lst[i])
    s+=1
    e+=1

print(max(conflicts))