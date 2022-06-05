def h(n):
    s=True
    for i in range(1,n+1):
        if i*i==n:
            s=False
        print(i)
    return s
