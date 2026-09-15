import sys
sys.stdin = open('lostcow.in','r')
sys.stdout = open('lostcow.out','w')
x,y = map(int,input().split())
d = -1/2
distTraveled = 0
pos = x
while True:
    d= int(-2*d)
    if min(pos,x+d) <= y <= max(pos,x+d):
        print(distTraveled+abs(pos-y))
        break
    else:
        distTraveled+=abs(pos-(x+d))
    pos = x+d
    