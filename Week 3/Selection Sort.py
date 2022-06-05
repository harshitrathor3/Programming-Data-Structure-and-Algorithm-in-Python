def SelectionSort(l):
    for i in range(len(l)):
        minpos=i
        for j in range(i,len(l)):
            if l[j]<l[minpos]:
                minpos=j
        l[i], l[minpos] = l[minpos], l[i]
    return l
