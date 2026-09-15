#nah, ima cry
#i had the correct implementation the VERY FIRST TRY, except for the fact that the problem says, ONCE A COW IS INFECTED, THEN THE K HANDSHAKES START COUNTING
#LITTERLY SCREWED OVER BY THE FINE PRINT
#AHHHHHHHHHHHHHHHH
#ok well lesson for next time is, especially on the problems where a human cant like instantly solve, and cases arent working, you are def misunderstanding the problem
#minor details can screw you over sooo much
#i was litterly thinking while implementing the shakes, hey this makes sense right?
#but if it is not directly stated in the problem, always double check

import sys
sys.stdin = open('tracing.in','r')
sys.stdout = open('tracing.out','w')
n,t = map(int,input().split())
cows = input()
shakes = sorted([list(map(int,input().split())) for i in range(t)])
def simulate(p0,k):
    shakeCount = [0 for i in range(n+1)]
    state = ['0' for i in range(n+1)]
    state[p0] = '1'
    for i in shakes:
        if state[i[1]] == '1':
            shakeCount[i[1]]+=1
        if state[i[2]] == '1':
            shakeCount[i[2]]+=1
        if state[i[1]] == '1' and shakeCount[i[1]] <= k:
            state[i[2]] = '1'
        if state[i[2]] == '1' and shakeCount[i[2]] <= k:
            state[i[1]] = '1'
    state.pop(0)
    return ''.join(state) == cows
p0 = set()
mink,maxk = float('inf'),-1

for i in range(1,n+1):
    for k in range(t+1):
        if simulate(i,k):
            p0.add(i)
            mink = min(mink,k)
            maxk = max(maxk,k)
x = len(p0)
y = mink
z = maxk
if z == t:
    z = 'Infinity'
print(x,y,z)