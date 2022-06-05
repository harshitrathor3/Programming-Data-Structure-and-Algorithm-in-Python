def length(l):
    if l==[]:
        return 0
    return 1+length(l[1:])
def lengthh(l):
    n=0
    for i in l:
       n+=1
    return n
