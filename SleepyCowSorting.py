import sys
sys.stdin = open('sleepy.in','r')
sys.stdout = open('sleepy.out','w')
n = int(input())
cows = list(map(int,input().split()))
ans = n-1
for i in reversed(range(n-1)):
    if cows[i] < cows[i+1]:
        ans = i
    else:
        break

print(ans)