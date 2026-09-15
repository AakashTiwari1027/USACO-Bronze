import sys
sys.stdin = open('backforth.in','r')
sys.stdout = open('backforth.out','w')
a = list(map(int,input().split()))
b = list(map(int,input().split()))
x,y = 0,0
p = set()
for t in a:
    for w in b+[t]:
        for th in a+[w]:
            if th ==t and x == 0:
                x+=1
                continue
            for f in b+[t,th]:
                if f == w and y == 0:
                    y+=1
                    continue
                p.add(1000-t+w-th+f)
            x,y = 0,0
print(len(p))