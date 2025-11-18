import math
def encryption(s):
    s=s.replace(" ","")
    n=len(s)
    root=math.sqrt(n)
    rows=math.floor(root)
    cols=math.ceil(root)
    
    if rows*cols<n:
        rows+=1
    result=[]
    for i in range(cols):
        word=""
        j=i
        while j<n:
            word+=s[j]
            j+=cols
        result.append(word)
    return " ".join(result)
s="haveaniceday"
print(encryption(s))
