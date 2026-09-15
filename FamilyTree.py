import sys
sys.stdin = open('family.in','r')
sys.stdout = open('family.out','w')
n,x,y = input().split()
n = int(n)
rel = [input().split() for i in range(n)]

def find_mother(x,lst):
    for i in rel:
        if i[1] == x:
            lst.append(i[0])
            find_mother(i[0],lst)
            break
a,b = [],[]
find_mother(x,a)
find_mother(y,b)

common_ancestor = False
for i in a:
    if i in b:
        common_ancestor = True
        break
if len(a) >= 1 and len(b) >= 1:
    if a[0] == b[0]:
        print('SIBLINGS')
        sys.exit()
if y in a:
    relation = ['great-']*(a.index(y))
    if len(relation) >= 1:
        relation[-1] = 'grand-'
    relation.append('mother')
    relation = ''.join(relation)
    print(f'{y} is the {relation} of {x}')
    sys.exit()
if x in b:
    relation = ['great-']*(b.index(x))
    if len(relation) >= 1:
        relation[-1] = 'grand-'
    relation.append('mother')
    relation = ''.join(relation)
    print(f'{x} is the {relation} of {y}')
    sys.exit()
if len(a) >= 1:
    if a[0] in b:
        relation = ['great-']*(b.index(a[0])-1)
        relation.append('aunt')
        relation = ''.join(relation)
        print(f'{x} is the {relation} of {y}')
        sys.exit()
if len(b) >= 1:
    if b[0] in a:
        relation = ['great-']*(a.index(b[0])-1)
        relation.append('aunt')
        relation = ''.join(relation)
        print(f'{y} is the {relation} of {x}')
        sys.exit()
if common_ancestor:
    print('COUSINS')
    sys.exit()
if common_ancestor == False:
    print('NOT RELATED')