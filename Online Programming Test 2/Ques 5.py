def listcommon(l1, l2):
    arr1, arr2 = [], []

    for i in l1:
        if i in l2:
            arr1.append(i)
    for i in l2:
        if i in l1:
            arr2.append(i)
