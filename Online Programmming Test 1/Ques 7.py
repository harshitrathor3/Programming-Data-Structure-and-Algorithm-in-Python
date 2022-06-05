arr=[]
while True:
    a = input()
    if a=='':
        break
    arr.append(a)

for i in range(len(arr)):
    if arr[0] not in arr[i]:
        print(arr[i])
