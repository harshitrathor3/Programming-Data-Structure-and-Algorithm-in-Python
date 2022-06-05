def sublist(l1, l):
    if len(l1)==0:
        return True
    if l1[0] in l:
        indx = l.index(l1[0])
        for i in range(len(l1)):
            print(l1[i], l[indx])
            if l1[i]!=l[indx]:
                return False
            indx+=1
        return True
    else:
        return False
