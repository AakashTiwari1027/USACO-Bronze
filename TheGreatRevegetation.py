import sys
sys.stdin = open('revegetate.in','r')
sys.stdout = open('revegetate.out','w')

n,m = map(int,input().split())
edges = [list(map(int,input().split())) for i in range(m)]

adj = [[] for i in range(n+1)]
colors = ['0' for i in range(n+1)]

for i in edges:
    adj[i[0]].append(i[1])
    adj[i[1]].append(i[0])

def works(node,color):
    for i in adj[node]:
        if colors[i] == str(color):
            return False
    return True

for i in range(1,n+1):
    for c in range(1,5):
        if works(i,c):
            colors[i] = str(c)
            break

colors.pop(0)
print(''.join(colors))


#Reason old code wasnt working, (See Timeline) was because 
#Consider we have three nodes:
#node 1 and 2 are the same, so we node2+=1
#then node 3 = node 2 so we have to up node 2 again right?
#my logic was that we couldnt decrease node 2 because then it would collide with something else, as we only increase when there is a collison
#what i didnt think about was that something could have changed node 1 before the node3/2 collison, so decreasing node 2 then become viable!
#general sol to take away from this is when bounds are small, and you smart sol aint working just brute force more dude