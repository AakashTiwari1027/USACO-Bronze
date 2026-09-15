#make observation that instead of h being the the range of 10^9 its the same as h being equal to one of the p[i], after that you can just check every value of h
#something that hinted towards this in the problem was that n = 1000 which is fairly low especially for a 2020 us open prob

n = int(input())
info = [input().split() for i in range(n)]
ans = []
for i in info:
    h = int(i[1])
    c = 0
    for a in range(n):
        if info[a][0] == 'L' and h > int(info[a][1]):
            c+=1
        if info[a][0] == 'G' and h < int(info[a][1]):
            c+=1
    ans.append(c)
print(min(ans))