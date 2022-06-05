def deldup(l):
    l1 = set(l)
    l2=list(l1)
    for i in l1:
        if l.count(i)>1:
            l2.remove(i)

    arr=[]
    for i in l:
        if i in l2:
            arr.append(i)
            l2.remove(i)
    return arr
