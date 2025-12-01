def mount(arr,k):
    arr.sort(reverse=True)
    total=0
    for i in range(len(arr)):
        total+=(i//k+1)*arr[i]
    return total
arr=[1,2,3,4]
k=3
print(mount(arr,k))
