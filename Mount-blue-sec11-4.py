def sherlock(arr):
    total_sum=0
    for i in range(len(arr)):
        total_sum+=arr[i]
    left_sum=0
    for i in range(len(arr)):
        if left_sum==total_sum-left_sum-arr[i]:
            return "YES"
        left_sum+=arr[i]
    return "NO"
arr=[5,6,8,11]
print(sherlock(arr))
