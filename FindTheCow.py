import sys
sys.stdin = open('cowfind.in','r')
sys.stdout = open('cowfind.out','w')
grass = input()
grass = grass[::-1]
c=  0
count = 0

for i in range(len(grass)-1):
    if grass[i]+grass[i+1] == '))':
        c+=1
    if grass[i]+grass[i+1] == '((':
        count+=c

print(count)