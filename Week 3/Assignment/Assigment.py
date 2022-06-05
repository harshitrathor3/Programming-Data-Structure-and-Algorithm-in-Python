def expanding(l):
    sb=abs(l[0]-l[1])
    for i in range(1,len(l)-1):
        #print(abs(l[i]-l[i+1]),sb)
        if abs(l[i]-l[i+1])<=sb:
            return False
        sb=abs(l[i]-l[i+1])
    return True
            
def sumsquare(l):
    smod=0
    smevn=0
    for i in l:
        if i%2==0:
            smevn+=i**2
        else:
            smod+=i**2
    return [smod,smevn]

def transpose(l):
    lst=[]
    if len(l[0])<=1:
        lst+=[[]]
        for i in l:
            lst[0]+=i
        return lst
    elif len(l)>1:
        for i in l[0]:
            lst.append([i])
        for i in range(len(l[1])):
            lst[i]+=[l[1][i]]
    return lst
