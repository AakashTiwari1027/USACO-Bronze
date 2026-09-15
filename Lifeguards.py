import sys
sys.stdin = open('lifeguards.in','r')
sys.stdout = open('lifeguards.out','w')
n = int(input())
guards = [list(map(int,input().split())) for i in range(n)]
time = [0 for i in range(1001)]
for i in guards:
    for j in range(i[0],i[1]):
        time[j]+=1
count = 1001-time.count(0)
p = []
for i in guards:
    c = 0
    for j in range(i[0],i[1]):
        if time[j] == 1:
            c+=1
    p.append(count-c)

print(max(p))