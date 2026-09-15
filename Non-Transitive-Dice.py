#alot of complete search

t = int(input())
dice = []
out = []
for i in range(t):
    inp = input().split()
    dice.append([list(map(int,inp[0:4])),list(map(int,inp[4:8]))])
    out.append('no')
for d1 in range(1,11):
    for d2 in range(1,11):
        for d3 in range(1,11):
            for d4 in range(1,11):
                c = [d1,d2,d3,d4]
                count = 0
                for i in dice:
                    c1,c2 = 0,0
                    for x in i[0]:
                        for y in i[1]:
                            if x>y:
                                c1+=1
                            if y>x:
                                c2+=1
                    if c1>c2:
                        a,b = i[0],i[1]
                    if c2>c1:
                        a,b = i[1],i[0]
                    if c1==c2:
                        continue
                    ac,ca,bc,cb = 0,0,0,0
                    for x in a:
                        for y in c:
                            if x>y:
                                ac+=1
                            if y>x:
                                ca+=1
                    for x in b:
                        for y in c:
                            if x>y:
                                bc+=1
                            if y>x:
                                cb+=1
                    if bc>cb and ca>ac:
                        out[count] = 'yes'
                    count+=1
                count = 0
for i in out:
    print(i)
