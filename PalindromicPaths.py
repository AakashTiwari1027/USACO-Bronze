#i did a different optimization strat then the sol, which was to prune the possibilities by checking if our patial string could possibly be a palindrom3
#this proved to be a lil slow on some testcases, and we got 4 tle's

import sys
sys.stdin = open('palpath.in','r')
sys.stdout = open('palpath.out','w')
n = int(input())
grid = [input() for i in range(n)]
palindromes = set()
size = 2*n-1

def generate(x,y,s,l):
    if 0 <= x < n and 0 <= y < n:
        s+=grid[y][x]
        if l > (size//2)+1:
            if grid[y][x] != s[size-l]:
                return
        if x == n-1 and y == n-1:
            if s == s[::-1]:
                palindromes.add(s)
            return
        generate(x+1,y,s,l+1)
        generate(x,y+1,s,l+1)

generate(0,0,'',1)
print(len(palindromes))