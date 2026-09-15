import sys
sys.setrecursionlimit(2**30)
sys.stdin = open('trapped.in','r')
sys.stdout = open('trapped.out','w')
n = int(input())
bales = sorted([list(map(int,input().split()))[::-1] for i in range(n)])
ans = 0
breakOut = False
def func(b1,b2):
    global breakOut
    if b1 < 0 or b2 >= n:
        breakOut = True
        return 
    power = bales[b2][0]-bales[b1][0]
    l,r = b1,b2
    if bales[b1][1] < power:
        l = b1-1
    if bales[b2][1] < power:
        r = b2+1
    if l == b1 and r == b2:
        return 
    func(l,r)

for i in range(n-1):
    breakOut = False
    func(i,i+1)
    if breakOut == False:
        ans+=bales[i+1][0]-bales[i][0]
print(ans)