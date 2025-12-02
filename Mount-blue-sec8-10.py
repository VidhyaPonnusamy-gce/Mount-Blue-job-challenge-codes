def fair_rotation(arr):
    count=0
    for i in range(len(arr)-1):
        if arr[i]%2!=0:
            arr[i]+=1
            arr[i+1]+=1
            count+=2
    if arr[-1]%2==0:
        return count
    else:
        return "NO"
arr=[2,3,4,5,6]
print(fair_rotation(arr))
