#implementation problem, thats all, had to debug a bit but it was fine
#code was pretty long which im not too happy about but whatever

import sys
sys.stdin = open('moocrypt.in','r')
sys.stdout = open('moocrypt.out','w')
n,m = map(int,input().split())
puzzle = [input() for i in range(n)]
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ans = []
dic = {}
for i in alpha:
    for j in alpha:
        dic[i+j] = 0

for y in range(n):
    for x in range(m):
        if 0 <= x+2 < m:
            s = puzzle[y][x]+puzzle[y][x+1]+puzzle[y][x+2]
            if s == s[0]+s[1]+s[1]:
                dic[s[0]+s[1]]+=1
            if s == s[2]+s[1]+s[1]:
                dic[s[2]+s[1]]+=1
            if s[::-1] == s[0]+s[1]+s[1]:
                dic[s[0]+s[1]]+=1
            if s[::-1] == s[2]+s[1]+s[1]:
                dic[s[2]+s[1]]+=1
        if 0 <= y+2 < n:
            s = puzzle[y][x]+puzzle[y+1][x]+puzzle[y+2][x]
            if s == s[0]+s[1]+s[1]:
                dic[s[0]+s[1]]+=1
            if s == s[2]+s[1]+s[1]:
                dic[s[2]+s[1]]+=1
            if s[::-1] == s[0]+s[1]+s[1]:
                dic[s[0]+s[1]]+=1
            if s[::-1] == s[2]+s[1]+s[1]:
                dic[s[2]+s[1]]+=1
        if 0 <= x+2 < m and 0 <= y+2 < n:
            s = puzzle[y][x]+puzzle[y+1][x+1]+puzzle[y+2][x+2]
            if s == s[0]+s[1]+s[1]:
                dic[s[0]+s[1]]+=1
            if s == s[2]+s[1]+s[1]:
                dic[s[2]+s[1]]+=1
            if s[::-1] == s[0]+s[1]+s[1]:
                dic[s[0]+s[1]]+=1
            if s[::-1] == s[2]+s[1]+s[1]:
                dic[s[2]+s[1]]+=1
        if 0 <= x+2 < m and 0 <= y-2 < n:
            s = puzzle[y][x]+puzzle[y-1][x+1]+puzzle[y-2][x+2]
            if s == s[0]+s[1]+s[1]:
                dic[s[0]+s[1]]+=1
            if s == s[2]+s[1]+s[1]:
                dic[s[2]+s[1]]+=1
            if s[::-1] == s[0]+s[1]+s[1]:
                dic[s[0]+s[1]]+=1
            if s[::-1] == s[2]+s[1]+s[1]:
                dic[s[2]+s[1]]+=1

max_ans = 0
for i in alpha:
    for j in alpha:
        if i != j:
            max_ans = max(max_ans,dic[i+j])
print(max_ans)