def foo(m):
    if m==0:
        return 0
    else:
        return m+foo(m-1)
