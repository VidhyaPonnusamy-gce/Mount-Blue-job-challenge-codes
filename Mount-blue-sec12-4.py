def sansaXor(arr):
    n=len(arr)
    result=0
    for i in range(n):
        count=(i+1)*(n-i)
        if count%2!=0:
            result^=arr[i]
    return result
arr=[3,4,5]
print(sansaXor(arr))
