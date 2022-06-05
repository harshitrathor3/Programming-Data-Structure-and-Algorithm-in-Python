def repeated(a, b, c, d):
    if a!=b:
        if b!=c:
            if c!=d:
                if a!=c:
                    if a!=d:
                        if b!=d:
                            return False
    return True

'''
Traceback (most recent call last):\n
  File "test.py", line 30, in <module>\n
    print(repeated(arglist[0],arglist[1],arglist[2],arglist[3]))\n
  File "test.py", line 13, in repeated\n
    return(result)\n
NameError: name 'result' is not defined
'''
