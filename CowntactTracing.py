import sys
sys.stdin = open('tracing.in','r')
sys.stdout = open('tracing.out','w')
n,t = map(int,input().split())
cows = input()
shakes = sorted([list(map(int,input().split())) for i in range(t)])
p0 = cows.count('1')

for i in range(n):
    if cows[i] == '1':
        for s in shakes:
            if s[1] == i+1:
                if cows[s[2]-1] == '0':
                    p0-=1
                break

lb,ub = [],'Infinity'

for i in range(n):
    if cows[i] == '1':
        c= 0
        for s in shakes:
            if s[1] == i+1:
                if cows[s[2]-1] == '1':
                    c+=1
                if cows[s[2]-1] == '0':
                    if c !=0:
                        ub = c
        lb.append(c)
lb = max(lb)
if ub != 'Infinity':
    lb = ub

print(p0,lb,ub)