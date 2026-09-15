#first try full testcases lets gooooooooooooo
#this problem was a breath of fresh air, it is part of a really old bronze content that i had litterly never done, (mind you i am doing this after being really nervous about usaco in general)
#the problem solving was fairly simple, as with a lot of these find state after time t problems you just had to find the state where it cycled, and take t mod n of that
#i knew this approach would work since num of states is only 2^16 (as every light is either on or off)
#during implemntation though, i couldnt add a the lst of states to a set, but because the lst is binary, i just converted it to a number and then added it which i am pretty proud of thinking of that
#i am now realizing i couldve just added the str of the lst into the set



import sys
sys.stdin = open('blink.in','r')
sys.stdout = open('blink.out','w')
n,t = map(int,input().split())
lights = [input() for i in range(n)]
states = set()
lst = []
count = 0
cycle = ''
def simulate(state):
    global count
    global cycle
    lst.append(state)
    states.add(int(state,2))
    count+=1
    if len(states) != count:
        cycle = state
        return
    l = ''
    for i in range(n):
        if state[i-1] == '1':
            if state[i] == '0':
                l+='1'
            else:
                l+='0'
        else:
            l+=state[i]
    simulate(l)

simulate(''.join(lights))

for i in range(len(lst)):
    if lst[i] == cycle:
        repeat = lst[i::]
        repeat.pop()
        break
if t < len(lst):
    ans = (lst[t])
else:
    ans = (repeat[(t-i)%len(repeat)])

for i in ans:
    print(i)