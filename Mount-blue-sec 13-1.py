def isValid(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    freq_count = {}
    for f in freq.values():
        freq_count[f] = freq_count.get(f, 0) + 1
    if len(freq_count) == 1:
        return "YES"  
    elif len(freq_count) == 2:
        f1, f2 = list(freq_count.keys())
        if (freq_count[f1] == 1 and (f1 - f2 == 1 or f1 - f2 == -1 or f1 == 1)) or \
           (freq_count[f2] == 1 and (f2 - f1 == 1 or f2 - f1 == -1 or f2 == 1)):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"
s="abccc"
print(isValid(s))
