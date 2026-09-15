#for every cow just calculate the total cost and tuition

n = int(input())
cows = sorted(list(map(int,input().split())))
list = []
tuition,amount = 0,1000001
for i in range(n):
    list.append([cows[i]*(n-i),cows[i]])
tuition = max(list)[0]
for i in list:
    if i[0] == tuition:
        if i[1] < amount:
            amount = i[1]
print(tuition,amount)