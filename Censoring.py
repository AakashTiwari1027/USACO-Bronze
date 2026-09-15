#embarrisingly easy problem imo

import sys
sys.stdin = open('censor.in','r')
sys.stdout = open('censor.out','w')
s = input()
word = input()
l = len(word)
censoredLen = 0
censored = ''
for i in s:
    censored+=i
    censoredLen+=1
    if censoredLen >= l:
        if (censored[censoredLen-l:censoredLen]) == word:
            censored = censored[0:censoredLen-l]
            censoredLen-=l
print(censored)