def timeInWords(h, m):
    nums = [
        "zero", "one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine", "ten", "eleven", "twelve",
        "thirteen", "fourteen", "quarter", "sixteen", "seventeen",
        "eighteen", "nineteen", "twenty", "twenty one", "twenty two",
        "twenty three", "twenty four", "twenty five", "twenty six",
        "twenty seven", "twenty eight", "twenty nine", "half"
    ]
    
    if m==0:
        return f"{nums[h]} o' clock"
    elif m==15:
        return f"quarter past {nums[h]}"
    elif m==30:
        return f"half past {nums[h]}"
    elif m==45:
        return f"quarter to {nums[h+1]}"
    elif m<30:
        if m==1:
            return f"one minute past {nums[h]}"
        else:
            return f"{nums[m]} minutes past {nums[h]}"
    else:
        mins=60-m
        if mins==1:
            return f"one minute to {nums[h+1]}"
        else:
            return f"{nums[mins]} minutes to {nums[h+1]}"
h=4
m=15
print(timeInWords(h,m))
