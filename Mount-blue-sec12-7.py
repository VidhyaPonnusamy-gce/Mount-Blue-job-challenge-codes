def matrix_flip(mat):
    n=len(mat)//2
    total=0
    for i in range(n):
        for j in range(n):
            total+=max(
                mat[i][j],
                mat[i][2*n-j-1],
                mat[2*n-i-1][j],
                mat[2*n-i-1][2*n-j-1]
            )
    return total
mat=[[1,2],[3,4]]
print(matrix_flip(mat))
