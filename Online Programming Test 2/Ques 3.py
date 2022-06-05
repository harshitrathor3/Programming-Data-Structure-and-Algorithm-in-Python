def increasing(l):
  if len(l) <= 1:
    return(True)
  else:
    print(l[0])
    return l[-1]>increasing(l[:-1])
