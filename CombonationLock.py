'''
ID: aakasht3
LANG: PYTHON3
TASK: combo
'''

import sys
sys.stdin = open('combo.in','r')
sys.stdout = open('combo.out','w')
n = int(input())
john = list(map(int,input().split()))
master = list(map(int,input().split()))
pj,pm = [],[]
nums = [i for i in range(1,n+1)]
for i in range(3):
    ji = nums.index(john[i])
    mi = nums.index(master[i])
    pj.append(list(set([nums[(ji-2)%n],nums[(ji-1)%n],nums[ji],nums[(ji+1)%n],nums[(ji+2)%n]])))
    pm.append(list(set([nums[(mi-2)%n],nums[(mi-1)%n],nums[mi],nums[(mi+1)%n],nums[(mi+2)%n]])))
overlap = 1
total = (2*(len(pj[0])**3))
for i in range(3):
    overlap = overlap*(len(pj[i]+pm[i])-len(set(pj[i]+pm[i])))
print(total-overlap)