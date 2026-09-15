n = int(input())
rel = [input().split() for i in range(n)]
rel = [[i[0],i[3],i[4],i[7]] for i in rel]
years = ['Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat']
cows = set()
for i in rel:
    cows.add(i[0])
    cows.add(i[-1])
cows = list(cows)
diffFromBessie = {i:-1 for i in cows}
cowYear = {i:'' for i in cows}
diffFromBessie['Bessie'] = 0
cowYear['Bessie'] = 'Ox'

for i in rel:
    year = cowYear[i[-1]]
    if i[1] == 'previous':
        if years.index(i[2]) < years.index(year):
            diffFromBessie[i[0]] = diffFromBessie[i[-1]]+(years.index(i[2])-years.index(year))
        else:
            diffFromBessie[i[0]] = diffFromBessie[i[-1]]+(-(12-(years.index(i[2])-years.index(year))))
    if i[1] == 'next':
        if years.index(year) < years.index(i[2]):
            diffFromBessie[i[0]] = diffFromBessie[i[-1]]+(years.index(i[2])-years.index(year))
        else:
            diffFromBessie[i[0]] = diffFromBessie[i[-1]]+(12-(years.index(year)-years.index(i[2])))
    cowYear[i[0]] = i[2]
print(abs(diffFromBessie['Elsie']))