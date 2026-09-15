import sys
sys.stdin = open('photo.in','r')
sys.stdout = open('photo.out','w')
n,k = map(int,input().split())
unfreindly = [list(map(int,input().split())) for i in range(k)]
lst = []
for i in range(k):
    lst.append([unfreindly[i][0],i])
    lst.append([unfreindly[i][1],i])
lst.sort()
count = 0
c = 0
s = set()
for i in lst:
    s.add(i[1])
    c+=1
    if len(s) != c:
        count+=1
        s = set()
        s.add(i[1])
        c = 1

print(count+1)