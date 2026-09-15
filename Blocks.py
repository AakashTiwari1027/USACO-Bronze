#brute force

from itertools import permutations
n = int(input())
blocks = [input() for i in range(4)]
words = [input() for i in range(n)]
pWords = []
out = ['NO' for i in range(n)]
for b1 in range(6):
    for b2 in range(6):
        for b3 in range(6):
            for b4 in range(6):
                str = (blocks[0][b1]+blocks[1][b2]+blocks[2][b3]+blocks[3][b4])
                perms = list(permutations(str))
                for i in perms:
                    s = (''.join(i))
                    pWords.append(s)
for p in pWords:
    for w in range(n):
        if words[w] in p:
            out[w] = 'YES'



for i in out:
    print(i)
