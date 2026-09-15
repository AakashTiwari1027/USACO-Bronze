#I LOVE MY LIFE
#EVERYTHING IS AWESOME
#i remember four score years ago that this problem made me cry, no clue how to solve it, thought i was doing everything right
#i came back, did it again, used my pro debugging skills, and OH BABY it WORKED
#main problem was we werent nesting our loop in a while loop, meaning at the end the end list may not have been equal

t = int(input())
out  = []

for _ in range(t):
    n = int(input())
    h = list(map(int,input().split()))
    c = 0
    impossible = False
    while impossible == False and len(set(h)) > 1:
        for i in range(n-1):
            d = abs(h[i]-h[i+1])
            if h[i] > h[i+1]:
                if i-1 < 0:
                    impossible = True
                    break
                h[i]-=d
                h[i-1]-=d
                c+=d
            if h[i+1] > h[i]:
                if i+2 > n-1:
                    impossible = True
                    break
                h[i+1]-=d
                h[i+2]-=d
                c+=d
    if impossible:
        out.append(-1)
        continue
    m = min(h)
    if m < 0:
        out.append(-1)
        continue
    out.append(2*c)

for i in out:
    print(i)