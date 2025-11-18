def organizingContainer(containers):
    n=len(containers)
    sum=[]
    for i in range(n):
        total=0
        for j in range(n):
            total+=containers[i][j]
        sum.append(total)
    type_sum=[]
    for i in range(n):
        total=0
        for j in range(n):
            total+=containers[i][j]
        type_sum.append(total)
    if sorted(sum)==sorted(type_sum):
        return "Possible"
    return "Impossible"
containers=[[1,1],[1,1]]
print(organizingContainer(containers))
        
