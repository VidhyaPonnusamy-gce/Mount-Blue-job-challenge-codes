class classname:
    def sum_xor(self,n):
        count=0
        for i in range(n):
            sums=n+i
            xor=n^i
            if sums==xor:
                count+=1
        return count
obj=classname()
print(obj.sum_xor(4))
