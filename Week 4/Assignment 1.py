def histogram(l):
    res={}
    for i in l:
        res[i]=count(l,i)
    ans=[]
    for i,i1 in res.items():
        ans+=[(i,i1)]
    ans.sort()
    ans.sort(key=lambda x:x[1])
    return ans

def count(l,i):
    cnt=0
    for i1 in l:
        if i1==i:
            cnt+=1
    return cnt

def getName(rolno, l):
    for i in range(len(l)):
        if l[i][0]==rolno:
            return l[i][1]

def subjCode(rolno, l):
    for i in range(len(l)):
        if l[i][0]==rolno:
            return l[i][1]

def subjName(code, l):
    for i in l:
        if i[0]==code:
            return i[1]

def transcript(cd, sd, t):
    res=[]
    for i in sd:
        lst=[]
        for j in t:
            if j[0]==i[0]:
                a=(j[1],subjName(j[1],cd),j[2])
                lst+=[a]
        lst.sort(key=lambda x:x[0])
        ans=(i[0],getName(i[0],sd),lst)
        res+=[tuple(ans)]
    res.sort(key = lambda x:x[0])
    return res
