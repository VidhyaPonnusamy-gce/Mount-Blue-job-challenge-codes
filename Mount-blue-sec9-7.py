def lady_ugs(b):
    f={}
    for i in b:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    if '_' not in b:
        for i in range(len(b)):
            if (i>0 and b[i]==b[i-1])or(i<len(b)-1 and b[i]==b[i+1]):
                continue
            else:
                return "NO"
        return "YES"
    for key ,value in f.items():
        if key!='_' and value==1:
            return "NO"
    return "YES"
b="RBY_YBR"
print(lady_ugs(b))
