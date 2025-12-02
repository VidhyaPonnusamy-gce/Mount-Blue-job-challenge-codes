def string_construction(s):
    s1=""
    count=0
    for i in s:
        if i not in s1:
            s1+=i
            count+=1
    return count
s="abcd"
print(string_construction(s))
