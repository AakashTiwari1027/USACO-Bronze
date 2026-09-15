nums = list(map(int,input().split()))
mask = [False for i in range(7)]

def same():
    t = []
    f = []
    for i in range(7):
        if mask[i]:
            t.append(nums[i])
        else:
            f.append(nums[i])
    t.sort()
    a,b,c = map(int,t)
    f.sort()
    if f == sorted([a+b,a+c,c+b,a+b+c]):
        return [a,b,c]
    else:
        return False

def recurse(curr,count):
    if curr == 7:
        return
    if count == 3:
        x = same()
        if x != False:
            print(x[0],x[1],x[2])
        return
    mask[curr] = True
    recurse(curr+1,count+1)
    mask[curr] = False
    recurse(curr+1,count)
recurse(0,0)
