import sys
sys.stdin = open('pails.in','r')
sys.stdout = open('pails.out','w')
x,y,m = map(int,input().split())
outs = []
for i in range(m//y+3):
    for j in range(m//x+3):
        if x*j + y*i <= m:
            outs.append(x*j + y*i)
print(max(outs))