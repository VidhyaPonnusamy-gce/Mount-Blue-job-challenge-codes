def funny_string(s):
    l=[]
    for i in range(len(s)):
        l=l+[ord(s[i])]
    l_result=[]
    for i in range(len(l)-1):
        l_result=l_result+[abs(l[i]-l[i+1])]
    s1=s[::-1]
    l2=[]
    for i in range(len(s1)):
        l2=l2+[ord(s1[i])]
    l2_result=[]
    for i in range(len(l2)-1):
        l2_result=l2_result+[abs(l2[i]-l2[i+1])]
    for i in range(len(l_result)):
        for j in range(len(l2_result)):
            if l_result[i]!=l2_result[i]:
                return "Not Funny"
    return "Funny"  
s="bcxz"
print(funny_string(s))
