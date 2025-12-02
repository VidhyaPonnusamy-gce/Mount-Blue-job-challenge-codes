def sherlock_feast(n):
    str=""
    fives=n
    while fives%3!=0 and fives>=0:
        fives-=5
    if fives<0:
        return -1
    else:
        str+="5"*fives
        str+="3"*(n-fives)
        print(str)
n=11
sherlock_feast(n)
