#Silver Prob
import sys
sys.stdin = open('rental.in','r')
sys.stdout = open('rental.out','w')

n,m,r = map(int,input().split())
cows = sorted([int(input()) for i in range(n)],reverse = True)
milk = sorted([list(map(int,input().split()))[::-1] for i in range(m)],reverse=True)
rent = sorted([int(input()) for i in range(r)],reverse=True)
money =[]

if r > n:
    rent = rent[0:n]
if r < n:
    for i in range(n-r):
        rent.append(0)

if m > n:
    milk = milk[0:n]
if m < n:
    for i in range(n-m):
        milk.append([0,0])
m = n
r = n

def sellMilk(m):
    global milk
    c = 0
    for i in range(m):
        if milk[i][1] > m:
            c+=((milk[i][0])*m)
            break
        else:
            c+=((milk[i][0])*milk[i][1])
            m-=milk[i][1]
    return c
s = sum(rent)
money.append(s)

for i in range(1,n):
    s-=rent[n-i]
    m = 0
    for j in range(i):
        m+=cows[j]
    money.append(s+sellMilk(m))

print(max(money))
