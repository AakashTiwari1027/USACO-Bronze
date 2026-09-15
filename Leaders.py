#there were alot of important observations in this one, being that the only viable leader pairs are a cow that has all cows and a cow that contains said cow, or 2 cows that contain
#all of there breed
#another optimizing observation was that the only cow that can contain all cows of its breed is the first cow of that breed

n = int(input())
cows = input()
e = list(map(int,input().split()))
pairs = 0
fg,lg = cows.index('G'),cows.rindex('G')
fh,lh = cows.index('H'),cows.rindex('H')
if e[fg]-1 >= lg:
    for i in range(fg):
        if cows[i] == 'H' and e[i]-1 >= fg:
            pairs+=1
if e[fh]-1 >= lh:
    for i in range(fh):
        if cows[i] == 'G' and e[i]-1 >= fh:
            pairs+=1
if e[fg]-1 >= lg and fg < fh:
    print(pairs+1)
    exit()
if e[fh]-1 >= lh and fh < fg:
    print(pairs+1)
    exit()
else:
    print(pairs)
