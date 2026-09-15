#LETS GOOOO
#ight so story for this problem was, it looked really simple (and in the end it was) but i just could not get this during my bronze practice
#so i came back to it today and was like bet, new challenge lets see if i improved
#the problem was kinda similar to connected components with dfs, but i didnt go down that path that much
#how i got the solution was basically this:
#if we plan to pass to cow i, first check if there is a cow who passes to cow i, repeat
#then, just pass to that cow, cuz its effectively the same as passing to cow i, except we cover one more cow
#this solution makes sense, because then its just the numbers of cows who no-one passes to, and duh, we have to supply a ball to them cuz if we dont who will
#so i coded that up and submitted
# 1/10 TESTCASES
#heh? was the aakash problem solving goat finally wrong?
#NOPE
#and i knew it wasnt wrong, so i plugged in a random test-case, and found the issue
#pretty neat edge case actually, if we have two cows that pass to eachother, and no one else passes to them, we need to supply a ball to them, but none of them have no passins
#so we checked for that case and got full tc baby
#holy yap

import sys
sys.stdin = open('hoofball.in','r')
sys.stdout = open('hoofball.out','w')
n = int(input())
cows = sorted(list(map(int,input().split())))
pass_to = [] 
passins = [0 for i in range(n)]
for i in range(n):
    if i == 0:
        pass_to.append(i+1)
        passins[i+1]+=1
        continue
    if i == n-1:
        pass_to.append(i-1)
        passins[i-1]+=1
        continue
    d1,d2 = abs(cows[i]-cows[i-1]),abs(cows[i]-cows[i+1])
    if d2 < d1:
        pass_to.append(i+1)
        passins[i+1]+=1
    if d1 <= d2:
        pass_to.append(i-1)
        passins[i-1]+=1
c = 0
for i in range(n-1):
    if pass_to[i] == i+1 and pass_to[i+1] == i:
        if passins[i] == 1 and passins[i+1] == 1:
            c+=1
print(c+passins.count(0))