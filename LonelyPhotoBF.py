n = int(input())
cows = list(input())
for i in range(n):
    if cows[i] == 'G':
        cows[i] = -1
    if cows[i] == 'H':
        cows[i] = 1
for i in range(1,n):
    cows[i]+=cows[i-1]
cows = [0]+cows

count = 0
for l in range(1,n+1):
    for r in range(l+2,n+1):
        length = r-l+1
        sum = cows[r]-cows[l-1]
        if sum == 2-(length) or sum == length-2:
            count+=1
            break

print(count)