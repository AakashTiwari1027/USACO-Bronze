import sys
sys.stdin = open('promote.in','r')
sys.stdout = open('promote.out','w')
levels = [list(map(int,input().split())) for i in range(4)]
promo = []
totala,totalb = 0,0
for i in reversed(range(4)):
    if i == 0:
        break
    totala+=levels[i][0]
    totalb+=levels[i][1]
    promo.append(totalb-totala)
for i in reversed(promo):
    print(i)