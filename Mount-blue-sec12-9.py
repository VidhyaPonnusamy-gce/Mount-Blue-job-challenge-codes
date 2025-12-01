def min_max(k,arr):
    arr.sort()
    min_diff=float('inf')
    for i in range(len(arr)-1):
        diff=arr[i+k-1]-arr[i]
        if diff<min_diff:
            min_diff=diff
    return min_diff
arr=[1,4,72]
k=2
print(min_max(k,arr))
