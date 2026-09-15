#i am actually so happy
#this is a exemplar problem showing how im gonna pass bronze this year
#its a bronze first of all, and i tried using a silver strategy (prefix sums) on it, showing that silver algo's work on some bronze
#but prefix sums timed out, so i just coded it the intended way
#i figured out HOW to get the sol and idk i just did it
#i knew on this type of problem i was supposed to fix the left and iterate forward and idk i litterly just did it
#i remember struggling so hard on this prob
n = int(input())
cows = list(input())
g,h = [],[]

for i in range(n):
    if cows[i] == 'G':
        g.append(i)
    if cows[i] == 'H':
        h.append(i)
g.append(n)
h.append(n)

ans = 0
for i in range(n):
    if cows[i] == 'G':
        if len(g) >= 2:
            photos = max(0,(g[1]-i+1)-3)
            ans+=photos
    if cows[i] == 'H':
        if len(h) >= 2:
            photos = max(0,(h[1]-i+1)-3)
            ans+=photos
    #ASSUME OPPOSITE TO BE ODD ONES OUT 
    if cows[i] == 'G':
        g.pop(0)
        if len(h) >= 2:
            h1,h2 = h[0],h[1]
            photos = h2-h1
            if h1 == i+1:
                photos-=1
            ans+=photos
    if cows[i] == 'H':
        h.pop(0)
        if len(g) >= 2:
            g1,g2 = g[0],g[1]
            photos = g2-g1
            if g1 == i+1:
                photos-=1
            ans+=photos
    
print(ans)