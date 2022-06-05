def mypalindrome(l):
  if l==[] or len(l) == 1:
    return(True)
  else:
    print(l)
    return(mypalindrome(l[:1])==mypalindrome(l[-1:-2:-1]))
