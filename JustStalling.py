# had to check stalls in order of the amoutn of stalls the biggest can go in, the the amount of stalls second biggest can go in -1 
# (cuz the biggest is in one of them)

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a = sorted(a, reverse = True)
count = 1
for i in range(n):
    c = 0
    for x in b:
        if a[i] <= x:
            c+=1
    count = count*(c-i)
print(count)