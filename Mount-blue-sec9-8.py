def counting_sort(arr):
    nums=[0]*len(arr)
    for num in arr:
        nums[num]+=1
    return nums
arr=[1,1,3,2,1]
print(counting_sort(arr))
