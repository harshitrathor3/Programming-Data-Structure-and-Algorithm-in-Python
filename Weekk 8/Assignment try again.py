n, k = map(int, input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
print(arr)
mx = sum(arr)
if arr[-1]<0:
    for i in range(1,k+1):
        l = arr[:len(arr)-i]
        sm = sum(l)
        print(l)
        if l[-i]<0:
            if sm>mx:
                mx = sm
        else:
            mx = sm
            break
print(mx)
