#It was really just greedy, you just had to decide wether to extend or make new subscription

n,k = map(int,input().split())
days = list(map(int,input().split()))
total = k+1
for i in range(1,n):
    total+=min(days[i]-days[i-1],k+1)
print(total)