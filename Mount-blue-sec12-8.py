def counter_game(n):
    turns=0
    while n>1:
        if (n&(n-1))==0:
            n//=2
        else:
            p=1
            while p*2<n:
                p*=2
            n-=p
        turns+=1
    return "Louise"if turns%2==1 else "Richard"
n=6
print(counter_game(n))
