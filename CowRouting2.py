import sys
sys.stdin = open('cowroute.in','r')
sys.stdout = open('cowroute.out','w')
a,b,n = map(int,input().split())
size = 100000
routes = [[list(map(int,input().split())),list(map(int,input().split()))] for i in range(n)]
atoc,btoc = [100000 for i in range(size)],[100000 for i in range(size)]

for i in routes:
    cost,cities = i[0][0],i[0][1]
    seenA = False
    seenB = False
    for j in i[1]:
        if j == a:
            seenA = True
            continue
        if seenA:
            atoc[j] = min(atoc[j],cost)
    for j in reversed(i[1]):
        if j == b:
            seenB = True
            continue
        if seenB:
            btoc[j] = min(btoc[j],cost)

answers = []
for i in routes:
    count = 0
    for j in i[1]:
        if j == a and count == 0:
            count+=1
        if j == b and count == 1:
            count+=1
    if count == 2:
        answers.append(i[0][0])

for i in range(size):
    answers.append(atoc[i]+btoc[i])
if min(answers) == 2*size:
    print(-1)
else:
    print(min(answers))