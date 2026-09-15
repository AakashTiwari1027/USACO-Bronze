#WOWWWWWWWWWWWW
#this is probably one of the most beautifully elegant solution i have ever done
#when i checked sol on this one i thought the sol was so stupid but i watched a yt video explaining it and mannnnn
#you simplify the string into T and F based on if the 2 len things have G in even or odd
#Than you simplify it again by condensing adjacent same letters into one letter, for example TFTTFFFFTT would be TFTFT
#drop the T from the end if there is one and than since string is alternating answer is just len of the string
#dang


n = int(input())
cows = input()
simplified = ''
for i in range(0,n,2):
    if cows[i]+cows[i+1] == 'GH':
        simplified+='F'
    if cows[i]+cows[i+1] == 'HG':
        simplified+='T'
simp = ''
for i in range(1,len(simplified)):
    if simplified[i] != simplified[i-1]:
        simp+=simplified[i-1]
if simplified[-1] == 'F':
    simp+='F'
print(len(simp))