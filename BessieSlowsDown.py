#one of our equations was wrong, but i caught it and got full tc

import sys
sys.stdin = open('slowdown.in','r')
sys.stdout = open('slowdown.out','w')
n = int(input())
events = [input().split() for i in range(n)]

times,dist = [float('inf')],[float('inf')]
for i in events:
    if i[0] == 'T':
        times.append(int(i[1]))
    if i[0] == 'D':
        dist.append(int(i[1]))
times.sort()
dist.sort()
speed = 1
distTraveled = 0
currTime = 0
eventsProcessed = 0

while eventsProcessed != n:
    if times[0]-currTime == (dist[0]-distTraveled)*speed:
        distTraveled = dist[0]
        currTime = times[0]
        speed+=2
        times.pop()
        dist.pop()
        eventsProcessed+=2
        continue
    if times[0]-currTime < (dist[0]-distTraveled)*speed:
        distTraveled+=(times[0]-currTime)/speed
        currTime = times[0]
        speed+=1
        times.pop(0)
        eventsProcessed+=1
        continue
    if times[0]-currTime > (dist[0]-distTraveled)*speed:
        currTime+=(dist[0]-distTraveled)*speed
        distTraveled = dist[0]
        speed+=1
        dist.pop(0)
        eventsProcessed+=1
currTime+=(1000-distTraveled)*speed

print(round(currTime))