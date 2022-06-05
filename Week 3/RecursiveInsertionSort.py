def InsertionSort(l):
    isort(l, len(l))
def isort(l, k):
    if k>1:
        isort(l, k-1)
        insert(l, k-1)
def insert(l, k):
    pos = k
    while pos>0 and l[pos]<l[pos-1]:
        l[pos], l[pos-1] = l[pos-1], l[pos]
        pos-=1
