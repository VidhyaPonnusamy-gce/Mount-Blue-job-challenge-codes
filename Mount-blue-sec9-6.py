def maximize(l,r):
    sums=0
    for i in range(l,r+1):
        for j in range(i,r+1):
            sums=max(sums,i^j)
    return sums
l=11
r=12
print(maximize(l,r))
