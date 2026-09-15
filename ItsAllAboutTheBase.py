#damn
#changing y > 0 to y > 9 really just saved the entire problem
#any error no matter how minute it might seem you should SO definatley change
import sys
from math import sqrt
sys.stdin = open('whatbase.in','r')
sys.stdout = open('whatbase.out','w')
k = int(input())
def quadratic(a,b,c):
    if (b**2)-(4*a*c) < 0:
        return 'imaginary'
    else:
        root = (-b+sqrt((b**2)-(4*a*c)))/(2*a) #positive root
        return root

for _ in range(k):
    a,b = map(str,input().split())
    for i in range(10,15001):
        x = (int(a[0])*(i**2))+(int(a[1])*(i))+int(a[2])
        y = quadratic(int(b[0]),int(b[1]),int(b[2])-x)
        if y != 'imaginary':
            if y > 9 and int(y) == y:
                print(i,int(y))
                break
