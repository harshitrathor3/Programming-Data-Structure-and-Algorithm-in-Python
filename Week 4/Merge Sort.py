def merge(a, b):
    c, i, j, = [], 0, 0
    m, n = len(a), len(b)

    while i+j<m+n:
        if i==m:
            c.append(b[j])
            j+=1
        elif j==n:
            c.append(a[i])
            i+=1
        elif a[i]<=b[j]:
            c.append(a[i])
            i+=1
        elif b[j]<a[i]:
            c.append(b[j])
            j+=1
    return c

def wrongmerge(a, b):
    c, i, j, = [], 0, 0
    m, n = len(a), len(b)
    while i+j<m+n:
        print(m,n,i,j)
        if i==m or b[j]<a[i]:
            c.append(b[j])
            j+=1
        elif j==n or a[i]<=b[j]:
            c.append(a[i])
            i+=1
    return c

def mergesort(a, l, r):
    if r-l <=1:
        return a[l:r]
    mid = (l+r)//2
    L = mergesort(a, l, mid)
    R = mergesort(a, mid, r)
    return merge(L, R)
