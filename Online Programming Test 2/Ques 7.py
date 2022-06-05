arr=[]
while True:
    inp = input()
    if inp=='':
        break
    arr.append(inp)
cnt=0
for i in set(arr[0]):
    for j in range(1, len(arr)):
        if i in arr[j]:
            cnt+=arr[j].count(i)
print(cnt)
