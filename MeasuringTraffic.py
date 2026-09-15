import sys
sys.stdin = open('traffic.in','r')
sys.stdout = open('traffic.out','w')
n = int(input())
sensors = [input().split() for i in range(n)]

a,b,c,d = 0,1000,0,1000
for i in sensors:
    if i[0] == 'on':
        a+=int(i[1])
        b+=int(i[2])
    if i[0] == 'off':
        a = max(a-int(i[2]),0)
        b = max(b-int(i[1]),0)
    if i[0] == 'none':
        a = max(a,int(i[1]))
        b = min(b,int(i[2]))

for i in reversed(sensors):
    if i[0] == 'on':
        c=max(c-int(i[2]),0)
        d = max(d-int(i[1]),0)
    if i[0] == 'off':
        c+=int(i[1])
        d+=int(i[2])
    if i[0] == 'none':
        c = max(c,int(i[1]))
        d = min(d,int(i[2]))
print(c,d)
print(a,b)