def getName(un, lst):
    for i in lst:
        if i[0]==un:
            return i[1]

def getTitle(acc, lst):
    for i in lst:
        if i[0]==acc:
            return i[1]

book = []
borow = []
chk = []
lst=[book, borow, chk]
i=0
s=''
while True:
    s=input()
    if s=='EndOfInput':
        break
    elif s=='Books':
        i=0
    elif s=='Borrowers':
        i=1
    elif s=='Checkouts':
        i=2
    lst[i].append(s.split('~'))
    
del book[0], borow[0], chk[0]
l=[]
for i in range(len(chk)):
    l.append([chk[i][2], getName(chk[i][0], borow), chk[i][1], getTitle(chk[i][1], book)])
l.sort()
for i in l:
    print(i[0], i[1], i[2], i[3],sep='~')
