import sys
sys.stdin = open('herding.in','r')
sys.stdout = open('herding.out','w')
lst = sorted(map(int,input().split()))
a,b,c = lst[0],lst[1],lst[2]
m,M = 2,0
if b == a+1 or b == a+2 or c == b+1 or c == b+2:
    m = 1
if [a,b,c] == [a,a+1,a+2]:
    m = 0

M = max(abs(a-b),abs(b-c))-1
print(m)
print(M)