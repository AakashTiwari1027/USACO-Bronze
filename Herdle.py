# kinda forgor if im honest. think it was pretty simple

answer,guess = [input() for i in range(3)],[input() for i in range(3)]
ansLetters,guessLetters = [],[]
for i in range(3):
    for a in range(3):
        ansLetters.append(answer[i][a])
        guessLetters.append(guess[i][a])
aLett = list(set(ansLetters))
gLett = [0 for i in range(len(aLett))]
yellowed = []
green,yellow = 0,0
for i in range(3):
    for a in range(3):
        if answer[i][a] == guess[i][a]:
            green+=1
            gLett[aLett.index(answer[i][a])]+=1
for i in range(3):
    for a in range(3):
        if guess[i][a] != answer[i][a] and guess[i][a] in ansLetters and guess[i][a] not in yellowed:
            yellow+=ansLetters.count(guess[i][a])-gLett[aLett.index(guess[i][a])]
            yellowed.append(guess[i][a])
print(green)
print(yellow)