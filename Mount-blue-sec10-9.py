def manasa(n,a,b):
    result=[]
    for i in range(n):
        value=i*b+(n-i-1)*a
        result=result+[value]
    return sorted(set(result))
n=3
a=1
b=2
print(manasa(n,a,b))
