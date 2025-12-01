def climbing(r,p):
    r=sorted(set(r),reverse=True)
    ranks=[]
    index=len(r)-1
    for i in p:
        while index>=0 and i>=r[index]:
            index-=1
        ranks.append(index+2)
    return ranks
r=[100,90,90,80]
p=[70,80,105]
print(climbing(r,p))
