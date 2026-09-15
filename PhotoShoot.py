import sys
sys.stdin = open('photo.in','r')
sys.stdout = open('photo.out','w')
n = int(input())
b = list(map(int,input().split()))
def gen(start):
    global b
    global n
    l = [start]
    for i in b:
        l.append(i-l[-1])
    if min(l) > 0 and max(l) <= n and len(set(l)) == len(l):
        return l
    else:
        return False
for i in range(1,n-1):
    if gen(i) != False:
        print(*gen(i))
        break