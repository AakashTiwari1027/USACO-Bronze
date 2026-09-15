#less goooo
#fairly simple implementation problem, im actually happy it didnt take up too many line of code
#not much to say, i was getting 4 tc wrong, but it was because i didnt put d under mod 4 (which i knew i was supposed to do!)
#regardless i debugged it pretty quick, pretty happy with my preformance on this problem

import sys
sys.stdin = open('ballet.in','r')
sys.stdout = open('ballet.out','w')
n = int(input())
moves = [input() for i in range(n)]

#define everything below to be in terms of (x,y)
feet = {'RL':[0,0],'RR':[1,0],'FL':[0,1],'FR':[1,1]}

movement = {'NF':[0,1],'NB':[0,-1],'NL':[-1,0],'NR':[1,0],
            'EF':[1,0],'EB':[-1,0],'EL':[0,1],'ER':[0,-1],
            'SF':[0,-1],'SB':[0,1],'SL':[1,0],'SR':[-1,0],
            'WF':[-1,0],'WB':[1,0],'WL':[0,-1],'WR':[0,1]}

dir = ['N','E','S','W']
d = 0
xpos,ypos = [0,1],[0,1]
f = ['FL','FR','RL','RR']
trip = False

for m in moves:
    foot = m[0]+m[1]

    if m[2] == 'P':
        x,y = map(int,feet[foot])
        for i in f:
            feet[i] = [x-(y-feet[i][1]),y+(x-feet[i][0])]
        d+=1
    else:
        feet[foot] = [feet[foot][0]+movement[dir[d%4]+m[2]][0],feet[foot][1]+movement[dir[d%4]+m[2]][1]]

    for i in range(4):
        for j in range(i+1,4):
            if feet[f[i]] == feet[f[j]]:
                print(-1)
                trip = True
                break
        if trip:
            break
    if trip:
        break

    for i in feet.values():
        xpos.append(i[0])
        ypos.append(i[1])

if not trip:
    print((max(xpos)-min(xpos)+1)*(max(ypos)-min(ypos)+1))