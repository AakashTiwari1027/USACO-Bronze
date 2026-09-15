#took a bit, but got the problem, fairly simple concept, all problem solving

import sys
sys.stdin = open('typo.in','r')
sys.stdout = open('typo.out','w')
s = input()
numOpen,numClosed = s.count('('),s.count(')')
if numClosed-numOpen == 2:
    closed = 0
    depth = 0
    for i in s:
        if i == '(':
            depth+=1
        if i == ')':
            depth-=1
            closed+=1
        if depth < 0:
            print(closed)
            break
if numOpen-numClosed == 2:
    depth = 0
    gthen2 = 0
    for i in s:
        if i == '(':
            depth+=1
        if i == ')':
            depth-=1
        if depth >= 2 and i == '(':
            gthen2+=1
    if s[-1] == '(':
        gthen2 = 1
    print(gthen2)
if numClosed-numOpen != 2 and numOpen-numClosed != 2:
    print(0)