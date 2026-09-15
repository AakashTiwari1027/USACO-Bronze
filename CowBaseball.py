import sys
sys.stdin = open('baseball.in','r')
sys.stdout = open('baseball.out','w')
n = int(input())
cows = [0]+sorted([int(input()) for i in range(n)])+[float('inf')]
def lower_bound(x): #least element greater than x
    lo,hi = 0,n+1
    while lo < hi:
        mid = (lo+hi)//2
        if cows[mid] >= x:
            hi = mid
        else:
            lo = mid+1
    return lo

def upper_bound(x): #greatest element less than x
    lo,hi = 0,n
    while lo < hi:
        mid = (lo+hi+1)//2
        if cows[mid] <= x:
            lo = mid
        else:
            hi = mid-1
    return hi
ans = 0
for x in range(1,n+1):
    for y in range(x+1,n+1):
        d= cows[y]-cows[x]
        ans+=(upper_bound(cows[y]+2*d)-lower_bound(cows[y]+d)+1)
print(ans)