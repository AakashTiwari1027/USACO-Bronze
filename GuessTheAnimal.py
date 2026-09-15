import sys
sys.stdin = open('guess.in','r')
sys.stdout = open('guess.out','w')
n = int(input())
animals = [input().split() for i in range(n)]
common =[ ]
for i in range(n):
    for a in range(i+1,n):
        common.append((int(animals[i][1])+int(animals[a][1]))-(len(set(animals[i][2::]+animals[a][2::]))))
print(max(common)+1)