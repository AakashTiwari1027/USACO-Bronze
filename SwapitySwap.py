import sys
sys.stdin = open('swap.in','r')
sys.stdout = open('swap.out','w')
n,k = map(int,input().split())
cows=[i+1 for i in range(n)]
a = list(map(int,input().split()))
b = list(map(int,input().split()))

def swap():
    global cows
    cows[a[0]-1:a[1]] = reversed(cows[a[0]-1:a[1]])
    cows[b[0]-1:b[1]] = reversed(cows[b[0]-1:b[1]])

copy = list(cows)
c = 1
swap()

while cows != copy:
    swap()
    c+=1
cows = copy
for i in range(k%c):
    swap()

for i in cows:
    print(i)