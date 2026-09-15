#good problem, def showed growth and debugging skills

k,n = map(int,input().split())
names = input().split()
papers = [input().split() for i in range(k)]
dic = {names[i]:i for i in range(n)}
ans = [['?' for i in range(n)] for j in range(n)]

for i in papers:
    lst = [i[0]]
    unsorted = False
    for j in range(1,n):
        if i[j] < i[j-1]:
            lst.append(i[j-1])
            unsorted = True
        if unsorted:
            for l in lst:
                ans[dic[l]][dic[i[j]]] = '0'
                ans[dic[i[j]]][dic[l]] = '1'
        if unsorted == False:
            lst.append(i[j])
for i in range(n):
    ans[i][i] = 'B'
for i in ans:
    print(''.join(i))
