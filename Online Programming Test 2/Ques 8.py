def studypairs(l):
    ans=[]
    l.sort()
    for i in range(len(l)):
        for j in range(i, len(l)):
            if abs(l[i][1]-l[j][1])>=10 and abs(l[i][2]-l[j][2])>=10:
                ans.append((l[i][0], l[j][0]))
    print(sorted(ans))
    return ans
    
