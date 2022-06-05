try:
    a=[1,2,3,4]
    a[1]
    a
    4/0
except IndexError:
    print("Index")
except NameError:
    print("Name")
except:
    print("Error")
