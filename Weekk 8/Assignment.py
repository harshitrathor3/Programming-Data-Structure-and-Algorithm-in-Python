def find_sum(l):
    l.sort(reverse=True)
    for i in range(k+1):
        global mx
        sm = sum(l[:len(l)-i])
        #print(l[:len(l)-i], sm)
        if sm>mx:
            mx = sm



def split():
    for i in range(len(arr)+1):
        for j in range(i+1, len(arr)+1):
            find_sum(arr[i:j])
            


n, k = map(int, input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))

mx=sum(arr)
split()
print(mx)
