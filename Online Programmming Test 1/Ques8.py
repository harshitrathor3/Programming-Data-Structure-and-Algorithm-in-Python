def aboveaverage(lst):
    phyavg, chmavg, matavg = 0, 0, 0
    phy, chm, mat = 0, 0, 0
    for i in lst:
        phy+=i[1]
        chm+=i[2]
        mat+=i[3]
    phyavg = phy/len(lst)
    chmavg = chm/len(lst)
    matavg = mat/len(lst)

    arr = [0]*len(lst)
    for i in range(len(lst)):
        if lst[i][1]>phyavg:
            arr[i]+=1
        if lst[i][2]>chmavg:
            arr[i]+=1
        if lst[i][3]>matavg:
            arr[i]+=1
    ans = []
    for i in range(len(lst)):
        if arr[i]>=2:
            ans+=[lst[i][0]]
    return ans
