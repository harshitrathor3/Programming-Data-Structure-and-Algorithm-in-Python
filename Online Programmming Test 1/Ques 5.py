def listdiff(l1, l2):
    arr1, arr2=[], []
    for i in l1:
        if i not in l2:
            arr1.append(i)

    for i in l2:
        if i not in l1:
            arr2.append(i)
    return [arr1, arr2]
