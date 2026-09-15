#now that i know trees this problem makes alot more sense, i have a reason behind the stuff im doing
import sys
sys.stdin = open('factory.in','r')
sys.stdout = open('factory.out','w')
n = int(input())
edges = [list(map(int,input().split())) for i in range(n-1)]
adj = [[] for i in range(n+1)]
for i in edges:
    adj[i[0]].append(i[1])
answers = []
for i in range(1,n+1):
    if adj[i] == []:
        answers.append(i)
if len(answers) == 1:
    print(answers[0])
else:
    print(-1)