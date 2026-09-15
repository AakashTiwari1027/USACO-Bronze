#SILVER PROB
import sys
sys.stdin = open('homework.in','r')
sys.stdout = open('homework.out','w')
n = int(input())
grades = list(map(int,input().split()))
sort = [[grades[i],i] for i in range(n)]
sort.sort()
avg = sum(grades)

pGrades = []

for i in range(n-2):
    if sort[0][1] == i:
        sort.pop(0)
    avg-=grades[i]
    pGrades.append((avg-sort[0][0])/(n-(i+1)))
m = max(pGrades)

for i in range(len(pGrades)):
    if pGrades[i] == m:
        print(i+1)