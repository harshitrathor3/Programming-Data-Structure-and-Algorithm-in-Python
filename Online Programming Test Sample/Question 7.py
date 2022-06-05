arr=[]
while True:
    inp = input()
    if inp=='':
        break
    arr.append(inp)

for i in range(0,len(arr),3):
    print(i)
