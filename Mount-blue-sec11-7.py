def permuting_array(arr1,arr2,k):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]+arr2[j]>=k:
                return "yes"
    else:
        return "no"
                
arr1=[1,2,2,1]
arr2=[3,3,3,4]
k=5
print(permuting_array(arr1,arr2,k))
