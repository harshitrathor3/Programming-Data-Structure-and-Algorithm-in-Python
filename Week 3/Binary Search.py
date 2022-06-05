def Binary_Search(seq, v, l, r):
    if r-l==0:
        return None, False
    mid = (l+r)//2
    if v==seq[mid]:
        return mid, True
    if v<seq[mid]:
        return Binary_Search(seq, v, l, mid)
    else:
        return Binary_Search(seq, v, mid+1, r)
