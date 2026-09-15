import sys
sys.stdin = open('greetings.in','r')
sys.stdout = open('greetings.out','w')
b,e = map(int,input().split())
bes = [input().split() for i in range(b)]
els = [input().split() for i in range(e)]
besMove,elsMove = [0],[0]
together = True
count = 0
for i in bes:
    for a in range(int(i[0])):
        if i[1] == 'L':
            besMove.append(besMove[-1]-1)
        if i[1] == 'R':
            besMove.append(besMove[-1]+1)
for i in els:
    for a in range(int(i[0])):
        if i[1] == 'L':
            elsMove.append(elsMove[-1]-1)
        if i[1] == 'R':
            elsMove.append(elsMove[-1]+1)
if len(besMove) < len(elsMove):
    besMove+=[besMove[-1] for i in range(len(elsMove)-len(besMove))]
if len(besMove) > len(elsMove):
    elsMove+=[elsMove[-1] for i in range(len(besMove)-len(elsMove))]


for i in range(min(len(besMove),len(elsMove))):
    if besMove[i] == elsMove[i]:
        if together == False:
            count+=1
        together = True
    if besMove[i] != elsMove[i]:
        together = False

print(count)
