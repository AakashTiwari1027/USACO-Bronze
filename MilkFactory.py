#ohhh, had to check sol on this one, graph problem, sol was just indentifying and counting sinks

import sys
sys.stdin = open('factory.in','r')
sys.stdout = open('factory.out','w')
n = int(input())
ways = [list(map(int,input().split())) for i in range(n-1)]
sink = []
for i in range(1,n+1):
    p = True
    for w in ways:
        if i == w[0]:
            p = False
            break
    if p == True:
        sink.append(i)
if len(sink) == 0 or len(sink) > 1:
    print(-1)
if len(sink) == 1:
    print(sink[0])