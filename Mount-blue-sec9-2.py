def cut_the_sticks(arr):
    arr.sort()
    n=len(arr)
    result=[n]
    for i in range(1,n):
        if arr[i]!=arr[i-1]:
            result.append(n-i)
    return result
arr=[5,4,4,2,2,8]
print(cut_the_sticks(arr))
