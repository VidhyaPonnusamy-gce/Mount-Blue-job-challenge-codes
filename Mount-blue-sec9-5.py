def game_throne(s):
    freq={}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    count=0
    for v in freq.values():
        if v%2!=0:
            count+=1
    if count>0:
        return "NO"
    else:
        return "YES"
        
s="aabbccdd"
print(game_throne(s))
