#good recursion prob

n = int(input())
a = list(map(int,input().split()))
k = int(input())
rec = [list(map(int,input().split())) for i in range(k)]
makeMore = True

def make(x):
    global makeMore
    r = -1
    for i in rec:
        if i[0] == x:
            r = i
            break
    if r == -1:
        makeMore = False
        return
    for i in r[2::]:
        if a[i-1] == 0:
            make(i)
        if makeMore == False:
            return
        a[i-1]-=1
    a[x-1]+=1

while makeMore:
    make(n)


print(a[n-1])