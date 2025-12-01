def recursive_digit(n,k):
    n=str(n)
    initial_sum=0
    for ch in n:
        initial_sum+=ord(ch)-ord('0')
    p=initial_sum*k
    while p>=10:
        sum=0
        while p!=0:
            digit=p%10
            sum+=digit
            p//=10
        p=sum
    return p
n=148
k=3
print(recursive_digit(n,k))
