#nice case work problem
n = int(input())
nums = list(map(int,input().split()))
o,e = 0,0
for i in nums:
    if i%2 == 0:
        e+=1
    else:
        o+=1

if o == e:
    print(2*e)
if e > o:
    print((2*o)+1)
while o > e:
    o-=2
    e+=1
    if o == e:
        print(2*e)
        break
    if e > o:
        print((2*o)+1)
        break
