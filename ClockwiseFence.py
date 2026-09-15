#ight so you kinda just had to know this problem, basically shape is in clockwise if sum of angles in 360, else ccw if -360
#i had another idea, which was to floodfill to know what segment was the inside, and then walk around the fence, see if the thing to your right is the internal segment
#think that would have worked

n = int(input())
out = []

for _ in range(n):
    dir = input()
    l = len(dir)
    sum = 0
    for i in range(l):
        s = dir[i]+dir[(i+1)%l]
        if s == 'NE' or s == 'ES' or s == 'SW' or s == 'WN':
            sum+=90
        if s == 'SE' or s == 'WS' or s == 'NW' or s == 'EN':
            sum-=90
    if sum == 360:
        out.append('CW')
    else:
        out.append("CCW")
for i in out:
    print(i)