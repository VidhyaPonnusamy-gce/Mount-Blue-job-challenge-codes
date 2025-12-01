def toys(k,n):
    n.sort()
    sum=0
    count=0
    for i in range(len(n)):
        sum+=n[i]
        if sum<k:
            count+=1
    return count
n=[1,12,5,111,200,1000,10]
k=50
print(toys(k,n))
