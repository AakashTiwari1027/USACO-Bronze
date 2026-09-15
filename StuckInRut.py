#LETS FINGGG GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#this problem actually traumatized me
#BUT I CAME BACK
#AND I DEBUGGED
#AND I GO FULL TEST CASESSSSSSSSSSSSSSSSSSSSS


n = int(input())
cows = []
for i in range(n):
    inp = input().split()
    cows.append([inp[0],int(inp[1]),int(inp[2])])
coll = []
ans = ['Infinity' for i in range(n)]
for i in range(n):
    for j in range(i+1,n):
        if cows[i][0] != cows[j][0]:
            N,E = 0,0
            if cows[i][0] == 'N':
                N,E = cows[i],cows[j]
            else:
                N,E = cows[j],cows[i]
            
            if N[1] > E[1] and E[2] > N[2]:
                if E[2]-N[2] > N[1]-E[1]:
                    ind = i
                    sind = j
                    if N == cows[j]:
                        ind = j
                        sind = i
                    coll.append([E[2]-N[2],ind,sind,N[1]-E[1]]) # time,  stoppedInd, stopperInd, how far stopper has to go to stop
                if N[1]-E[1] > E[2]-N[2]:
                    ind = i
                    sind = j
                    if E == cows[j]:
                        ind = j
                        sind = i
                    coll.append([N[1]-E[1],ind,sind,E[2]-N[2]]) # time, stoppedInd, stopperInd, how far stopper has to go to stop
coll.sort()
for i in coll:
    if ans[i[1]] == 'Infinity' and i[0] != 'X': #stopped had no earlier collisions
        ans[i[1]] = i[0]
        for j in range(len(coll)):
            if coll[j][2] == i[1]:
                if coll[j][3] > i[0]:
                    coll[j][0] = 'X'
for i in ans:
    print(i)