def closestNumber(arr):
    arr.sort()
    l=[]
    min_diff=abs(arr[1]-arr[0])
    for i in range(1,len(arr)):
        diff=abs(arr[i]-arr[i-1])
        if diff<min_diff:
            min_diff=diff
    for i in range(1,len(arr)):
        if abs(arr[i]-arr[i-1])==min_diff:
            l=l+[arr[i-1],arr[i]]
    return l
arr=[2,3,4,5]
print(closestNumber(arr))
