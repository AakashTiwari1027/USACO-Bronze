#so easy i litterly solved it in 6 mins cuh
import sys
sys.stdin= open('speeding.in','r')
sys.stdout = open('speeding.out','w')
n,m = map(int,input().split())
road = [list(map(int,input().split())) for i in range(n)]
cow = [list(map(int,input().split())) for i in range(m)]

diff = [0 for i in range(100)]
lc,bc = 0,0

for i in cow:
    count = bc
    for j in range(count,count+i[0]):
        diff[j]+=i[1]
    bc = count+i[0]

for i in road:
    count = lc
    for j in range(count,count+i[0]):
        diff[j] -= i[1]
    lc+=i[0]

print(max(max(diff),0))