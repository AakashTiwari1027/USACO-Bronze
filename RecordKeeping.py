import sys
sys.stdin = open("records.in","r")
sys.stdout = open('records.out','w')
n = int(input())
cows = [sorted(input().split()) for i in range(n)]
count = []
for i in cows:
    count.append(cows.count(i))
print(max(count))