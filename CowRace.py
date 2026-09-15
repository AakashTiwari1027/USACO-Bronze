import sys
sys.stdin = open("cowrace.in","r")
sys.stdout = open('cowrace.out','w')
n,m = map(int,input().split())
b = [list(map(int,input().split())) for i in range(n)]
e = [list(map(int,input().split())) for i in range(m)]
br,er = [0],[0]
for i in range(n):
    for t in range(b[i][1]):
        br.append(br[-1]+b[i][0])
for i in range(m):
    for t in range(e[i][1]):
        er.append(er[-1]+e[i][0])
lead = [0]
count = 0
for i in range(len(br)):
    if br[i] > er[i] and lead[-1] != 'b':
        count+=1
        lead.append('b')
    if er[i] > br[i] and lead[-1] != 'e':
        count=+1
        lead.append('e')

print(len(lead)-2)