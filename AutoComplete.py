import sys
sys.stdin = open('auto.in','r')
sys.stdout = open('auto.out','w')
w,n = map(int,input().split())
words = [['',-1]]+sorted([[input(),i+1] for i in range(w)])+[['z'*(1000001),w]]
partial = [input().split() for i in range(n)]
def lower_bound(x): #least element greater (or equal to) than x
    lo,hi = 0,w+1
    while lo < hi:
        mid = (lo+hi)//2
        if words[mid][0][0:len(x)] >= x:
            hi = mid
        else:
            lo = mid+1
    return lo

for i in partial:
    pre = i[1]
    k = int(i[0])
    ind = lower_bound(pre)
    exist = False
    if 1 <= ind+k < w+1:
        if words[ind+k-1][0][0:len(pre)] == pre:
            print(words[ind+k-1][-1])
            exist = True
    if exist == False:
        print(-1)


