def cavity_map(grid):
   n=len(grid)
   grid=list(grid)
   result=grid[:]
   for i in range(1,n-1):
       for j in range(1,n-1):
           val=grid[i][j]
           if (val>grid[i-1][j] and
               val>grid[i+1][j] and
               val>grid[i][j-1] and
               val>grid[i][j+1]):
               result[i]=result[i][:j]+'X'+result[i][j+1:]
   return result
grid=['1112','1912','1892','1234']
print(cavity_map(grid))
