#this problem is pretty similar to a problem papa gave me about wire length optimization so that was cool
#im proud that i thought of a good way to implement, which was swapping pairs of cows until we reach the optimal solution (any swap on the optimal will result in a worse or equal solution)
#getting two tc wrong, but still pretty happy
#bit worried that this approach just got lucky, but seems to work. yeah this approach was a greedy strat, which doesnt work for all cases

import sys
sys.stdin = open('haywire.in','r')
sys.stdout = open('haywire.out','w')
n = int(input())
friends = [list(map(int,input().split())) for i in range(n)]

def evaluate(lst):
    inv = [0]*(n)
    for i in range(n):
        inv[lst[i]-1] = i
    wire = 0
    for i in range(n):
        for j in friends[i]:
            wire+=abs(inv[i]-inv[j-1])
    return wire//2

lst = [i+1 for i in range(n)]
while True:
    swapped = []
    ogEval = evaluate(lst)
    for i in range(n):
        for j in range(i+1,n):
            a = lst[i]
            b = lst[j]
            copy = list(lst)
            copy[i] = b
            copy[j] = a
            swapped.append([evaluate(copy),copy])
    swapped.sort()
    if swapped[0][0] >= ogEval:
        print(ogEval)
        break
    lst = swapped[0][1]

