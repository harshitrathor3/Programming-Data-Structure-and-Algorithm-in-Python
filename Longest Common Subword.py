def LCW(u, v):
    
    for r in range(len(u)+1):
        a[r][len(v)+1]=0
    for c in range(len(v)+1):
        a[len(u)+1][c]=0
    print(a)
    
