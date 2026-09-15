#ima just write the analysis now cuz ill forget later
#this problem was so frustrating cuz it was just deciptivley easy
#so i got the cases where you place the cows in the center of the gap and 1/3 of the way in the gap
#but it was completley failing
#i plugged in some testcases, utilizing another brute force solution, and found an edge case
#basically if its all zeros, it would count it as one gap, when it should have placed the cows on the leftmost and rightmost end
#unfortunatley i took this to be a one-off edgecase, and didnt realize its general application to the problem which was the other case
#000000100000, where you ALSO place on the left and right
#sum of the story here is to dwell on you edge cases a little, some may be immediatly obvious to be generally applied, but when it looks like its a one-off, think a little, and try more
#cases like that

import sys
from math import floor, ceil
sys.stdin = open('socdist1.in','r')
sys.stdout = open('socdist1.out','w')
n = int(input())
cows = input()
gaps = []
c = 0
for i in cows:
    if i == '0':
        c+=1
    if i == '1':
        gaps.append(c)
        c = 0
if c != 0:
    gaps.append(c)
gaps.pop(0)

def center_greatest(s):
    l,r = [],[]
    c = 0
    for i in s:
        c+=1
        if i == '1':
            c = 0
        l.append(c)
    c = 0
    for i in reversed(s):
        c+=1
        if i == '1':
            c = 0
        r.append(c)
    d = [min(l[i],r[n-i-1]) for i in range(n)]
    m = max(d)
    return d.index(m)
def solve(x):
    gaps = []
    c= 0
    for i in range(n):
        if x[i] == '0':
            c+=1
        if x[i] == '1':
            gaps.append(c)
            c = 0
    if c != 0:
        gaps.append(c)
    gaps.pop(0)
    return min(gaps)
ans = []
#LC
copy = list(cows)
if copy[0] == '0':
    copy[0] = '1'
    copy[center_greatest(copy)] = '1'
    ans.append(solve(copy))
#RC
copy = list(cows)
if copy[-1] == '0':
    copy[-1] = '1'
    copy[center_greatest(copy)] = '1'
    ans.append(solve(copy))
#CC
copy = list(cows)
copy[center_greatest(copy)] = '1'
copy[center_greatest(copy)] = '1'
ans.append(solve(copy))
#LR
copy = list(cows)
if copy[0] == '0' and copy[-1] == '0':
    copy[0] = '1'
    copy[-1] = '1'
    ans.append(solve(copy))
#2/3
c2 = sorted(gaps,reverse=True)
a = c2.pop(0)
if (a-2)%3 == 0:
    c2+=[(a-2)/3,(a-2)/3,(a-2)/3]
elif (a-2)%3 == 1:
    c2+=[floor((a-2)/3),floor((a-2)/3),ceil((a-2)/3)]
else:
    c2+=[ceil((a-2)/3),ceil((a-2)/3),floor((a-2)/3)]
ans.append(min(c2))
print(int(max(ans)+1))