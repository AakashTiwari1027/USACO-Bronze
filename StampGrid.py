#Complex complete search, implementation problems were just finding out how to make a copy of a list that doesnt change with the
#copied one


t = int(input())
out = []
def Stamp(x,y,stamp,k,canvas):
    canv = [[canvas[a][i] for i in range(n)] for a in range(n)]
    for i in range(k):
        for a in range(k):
            if stamp[a][i] == '*':
                canv[y+a][x+i] = '*'
    return canv
for T in range(t):
    input()
    n = int(input())
    paint = [input() for i in range(n)]
    k = int(input())
    stamp = [input() for i in range(k)]
    canvas = [['.' for i in range(n)] for i in range(n)]
    blank = []
    for i in range(n):
        for a in range(n):
            if paint[i][a] == '.':
                blank.append([i,a])
    for i in range(4):
        stamp = [''.join(row) for row in zip(*reversed(stamp))]
        for a in range(n-k+1):
            for b in range(n-k+1):
                p = Stamp(a,b,stamp,k,canvas)
                for c in blank:
                    if p[c[0]][c[1]] == '*':
                        p = False
                        break
                if p!=False:
                    canvas = p
    for i in range(n):
        canvas[i] = ''.join(canvas[i])
    if paint == canvas:
        out.append('YES')
    else:
        out.append('NO')
for i in out:
    print(i)