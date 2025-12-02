def smart_number(n):
    count=0
    for i in range(1,n):
        if n%i==0:
            count+=1
    if count%2==0:
        return "YES"
    else:
        return "NO"
n=169
print(smart_number(n))
