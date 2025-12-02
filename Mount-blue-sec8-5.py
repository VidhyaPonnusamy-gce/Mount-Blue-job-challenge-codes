def find_digit(n):
    count=0
    temp=n
    while temp>0:
        digit=temp%10
        if digit!=0 and n%digit==0:
            count+=1
        temp//=10
    return count     
n=10
print(find_digit(n))
