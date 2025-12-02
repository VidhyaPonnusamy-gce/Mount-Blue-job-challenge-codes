def palin(s):
    if s==s[::-1]:
        return 0
    i=0
    j=len(s)-1
    while i<j:
        if s[i+1:j+1]==s[i+1:j+1][::-1]:
            return i
        elif s[i:j]==s[i:j][::-1]:
            return j
        i+=1
        j-=1
    return -1
s="aaab"
print(palin(s))
