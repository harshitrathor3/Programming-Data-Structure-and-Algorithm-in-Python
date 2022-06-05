def listdup(l):
    arr=[]
    for i in l:
        if l.count(i)>1:
            if i not in arr:
                arr.append(i)
    return arr
