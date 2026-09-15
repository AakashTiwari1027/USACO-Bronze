#make the realization the the only top left square that could flip the bottom right is the entire square, go from there

import sys
sys.stdin = open('cowtip.in','r')
sys.stdout = open('cowtip.out','w')
n = int(input())
cows = [list(input()) for i in range(n)]
count = 0
def tip(h,w):
    global cows
    for i in range(h):
        for a in range(w):
            if cows[i][a] == '1':
                cows[i][a] = '0'
            else:
                cows[i][a] = '1'
for i in reversed(range(n)):
    for a in reversed(range(n)):
        if cows[i][a] == '1':
            tip(i+1,a+1)
            count+=1
print(count)