def gamingArray(arr):
    seen=-1
    moves=0
    for num in arr:
        if num>seen:
            seen=num
            moves+=1
    return "BOB" if moves%2==1 else "ANDY"
arr=[5,2,6,3,4]
print(gamingArray(arr))
