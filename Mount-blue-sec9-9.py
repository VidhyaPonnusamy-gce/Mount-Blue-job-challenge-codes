def priyanka_toys(arr):
    arr.sort()
    min_wght=arr[0]
    count=1
    for i in arr:
        if i>min_wght+4:
            count+=1
            min_wght=i
    return count
arr=[1,2,3,21,7,12,14,21]
print(priyanka_toys(arr))
