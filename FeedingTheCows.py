# got it on second try, sol was just different approach to what i was doing. key observations was that the optimal place to place a 
# grass if you needed it is to place it at i+k. i got that much, i just had to figure out if a cow needed grass or not. the correct
# way to check if a cow needed grass is to see if it is in range of last grass using a variable

t = int(input())
out = []
for T in range(t):
    n,k = map(int,input().split())
    cows = input()
    G,H = [],[]
    gcover,hcover = -1,-1
    grass = ['.' for i in range(n)]
    for i in range(n):
        if cows[i] == 'G':
            G.append(i)
        if cows[i] == 'H':
            H.append(i)
    for i in range(n):
        max = i+k
        if max > n-1:
            max = n-1
        if cows[i] == 'G':
            if gcover < i:
                if grass[max] == '.':
                    grass[max] = 'G'
                    gcover = i+2*k
                else:
                    grass[max-1] = 'G'
                    gcover = (i+2*k)-1
        if cows[i] == 'H':
            if hcover < i:
                if grass[max] == '.':
                    grass[max] = 'H'
                    hcover = i+2*k
                else:
                    grass[max-1] = 'H'
                    hcover = (i+2*k)-1
    out.append(n-grass.count('.'))
    out.append(''.join(grass))
for i in out:
    print(i)