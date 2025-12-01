def anagram(s1,s2):
   freq={}
   for i in s1:
       if i in freq:
           freq[i]+=1
       else:
           freq[i]=1
   freq_1={}
   for i in s2:
       if i in freq_1:
           freq_1[i]+=1
       else:
           freq_1[i]=1
   letters=set(freq.keys()).union(set(freq_1.keys()))
   dels=0
   for ch in letters:
       count1=freq.get(ch,0)
       count2=freq_1.get(ch,0)
       dels+=abs(count1-count2)
   return dels
s1="abc"
s2="amnop"
print(anagram(s1,s2))
