n,s = map(int,input().split())
s-=1
line = [list(map(int,input().split())) for i in range(n)]

broken = 0
j0 = 0
def bounce(pos,pow,dir):
    global broken
    global line
    global j0
    if pos < 0 or pos >= len(line) or j0 == 997:
        return
    if line[pos][0] == 1:
        if line[pos][1] <= pow:
            broken+=1
            line[pos][0] = -1
    if line[pos][0] == 0:
        dir = (dir+1)%2
        pow+=line[pos][1]
    j0+=1
    if dir == 0:
        bounce(pos+pow,pow,dir)
    if dir == 1:
        bounce(pos-pow,pow,dir)

bounce(s,1,0)
print(broken)