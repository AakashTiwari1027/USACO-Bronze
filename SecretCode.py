#this was a good problem for debugging, got the idea pretty easily, but i had loose definitions
#i used random strat quite a bit and it worked very well
#full testcases baby
import sys
sys.stdin = open('scode.in','r')
sys.stdout = open('scode.out','w')
s = input()
count = 0

def recurse(state,waysToMake):
    global count
    length = len(state)
    Set = set()
    Set.add(state[0:(length//2)+1])
    Set.add(state[(length//2):length])
    for s in Set:
        c = 0
        if s+s[1::] == state:
            c+=1
        if s[1::]+s == state:
            c+=1
        if s+s[0:len(s)-1] == state:
            c+=1
        if s[0:len(s)-1]+s == state:
            c+=1
        if len(s) > 2:
            recurse(s,c*waysToMake)
        count+=c*waysToMake

recurse(s,1)
print(count)