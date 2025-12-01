def median(arr):
    arr.sort()
    n=len(arr)//2
    return arr[n]
arr=[0,1,2,4,6,5,3]
print(median(arr))
