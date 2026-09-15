import sys
sys.stdin = open('tttt.in','r')
sys.stdout = open('tttt.out','w')
board = [input() for i in range(3)]
solo,team = set(),set()
for i in range(3):
    if len(set(board[i])) == 1:
        solo.add(str(set(board[i])))
    if len(set(board[i])) == 2:
        team.add(str(set(board[i])))
for i in range(3):
    string = ''
    for a in range(3):
        string+=board[a][i]
    if len(set(string)) == 1:
        solo.add(str(set(string)))
    if len(set(string)) == 2:
        team.add(str(set(string)))
d1 = board[0][0]+board[1][1]+board[2][2]
d2 = board[0][2]+board[1][1]+board[2][0]
if len(set(d1)) == 1:
    solo.add(str(set(d1)))
if len(set(d2)) == 1:
    solo.add(str(set(d2)))
if len(set(d1)) == 2:
    team.add(str(set(d1)))
if len(set(d2)) == 2:
    team.add(str(set(d2)))
print(len(solo))
print(len(team))