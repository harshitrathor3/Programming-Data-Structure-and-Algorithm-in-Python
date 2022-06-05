def factors(num):
    flist=[]
    for i in range(2,num):
        if num%i==0:
            flist = flist + [[i,num//i]]
    return flist
            

def isprime(n):
    if n!=2 and n%2==0:
        return False
    else:
        for i in range(3,n,2):
            if n%i==0:
                return False
        else:
            return True

def primeproduct(n):
    if n<0:
        return False
    flist=factors(n)
    for i in flist:
        if isprime(i[0]) and isprime(i[1]):
            return True
    else:
        return False


def delchar(s,c):
    if len(c)!=1:
        return s
    new=''
    for i in s:
        if i!=c:
            new+=i
    return new

'''
def shuffle(l1,l2):
    newlst=[]
    for i in range(min(len(l1),len(l2))):
        newlst = newlst + [l1[i]] + [l2[i]]
    if len(l1)>len(l2):
        newlst = newlst + l1[i+1:]
    elif len(l2)>len(l1):
        newlst = newlst + l2[i+1:]
    return newlst
'''
def shuffle(l1,l2):
    newlst=[]
    for i in range(min(len(l1),len(l2))):
        newlst = newlst + [l1.pop(0)] + [l2.pop(0)]
    newlst = newlst + l1 + l2
    return newlst
