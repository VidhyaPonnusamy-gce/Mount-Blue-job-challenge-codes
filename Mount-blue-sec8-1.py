def taum(b,w,bc,wc,z):
    cost1=min(bc,wc+z)
    cost2=min
    (wc,bc+z)
    total=b*cost1+w*cost2
    return total
print(taum(3,5,3,4,1))
