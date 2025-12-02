def anagram(s):
    if len(s)%2!=0:
        return -1
    n=len(s)//2
    s1=s[:n]
    s2=s[n:]
    count=0
    freq={}
    for i in s1:
        freq[i]=freq.get(i,0)+1
    for i in s2:
        if i in freq and freq[i]>0:
            freq[i]-=1
        else:
            count+=1
    return count
s="xyyx"
print(anagram(s))
