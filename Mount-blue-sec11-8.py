def miss_num(arr1,arr2):
    freq={}
    for i in arr1:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    freq1={}
    for i in arr2:
        if i in freq1:
            freq1[i]+=1
        else:
            freq1[i]=1
    miss=[]
    for key in freq1:
        if key not in freq or freq1[key]>freq[key]:
            miss.append(key)
    miss.sort()
    return miss
arr1=[1,2,3,4,5]
arr2=[1,2,6,7,5]
print(miss_num(arr1,arr2))
