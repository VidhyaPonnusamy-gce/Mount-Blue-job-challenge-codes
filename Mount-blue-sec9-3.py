def kaprekar(p,q):
    found=False
    for i in range(p,q+1):
        sq=str(i*i)
        n=len(str(i))
        right=int(sq[-n:]) if sq[-n:] else 0
        left=int(sq[:-n]) if sq[:-n] else 0
        if left+right==i:
            print(i,end=" ")
            found=True
    if not found:
        return "No valid kaprekar number"
p=1
q=100
kaprekar(p,q)
