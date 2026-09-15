#this problem was so sad very bad
#again, cuz of my problem solving goatness i got the word for word band for band correct solution
#but
#when i implemented it, i only ran through n times
#when really i should have nested the for loop in a while loop, cuz we could come back to the first one after deleting other ones to make it possible!
#i think i made this same type of nesting mistake on a acowdemia problem
#so yeah beware of this
#dude im realizing now that during problem solving i was thinking of implementing it with a while loop, that would break out when all things are deleted
#which isnt really the right idea
#but still if i didnt ignore that thought i would have been balling and not bawling


t = int(input())
out = []
for _ in range(t):
    input()
    n,m = map(int,input().split())
    inp = [input().split() for i in range(m)]
    removed = [False for i in range(m)]
    program = []
    rem = 0
    looping = True
    while looping:
        change= 0
        for loc in range(n):
            out1,out0 = set(),set()
            ind1,ind0 = [],[]

            for s in range(m):
                if removed[s]:
                    continue
                if inp[s][0][loc] == '1':
                    out1.add(inp[s][1])
                    ind1.append(s)
                if inp[s][0][loc] == '0':
                    out0.add(inp[s][1])
                    ind0.append(s)
            if len(out1) == 1:
                program.append([loc,'1',list(out1)[0]])
                for i in ind1:
                    removed[i] = True
                    rem+=1
                    change+=1
            if len(out0) == 1:
                program.append([loc,'0',list(out0)[0]])
                for i in ind0:
                    removed[i] = True
                    rem+=1
                    change+=1
        if change == 0:
            break

    if rem == m:
        out.append('OK')
    else:
        out.append('LIE')
for i in out:
    print(i)
