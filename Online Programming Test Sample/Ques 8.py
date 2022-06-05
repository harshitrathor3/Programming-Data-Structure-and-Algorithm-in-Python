def repeated(l):
    cnt=0
    for i in set(l):
        if l.count(i)>1:
            cnt+=1
    return cnt
