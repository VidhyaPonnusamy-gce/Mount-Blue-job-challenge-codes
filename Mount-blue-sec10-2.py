def insertion_sort1(arr):
    key=arr[-1]
    i=len(arr)-2
    while i>=0 and arr[i]>key:
        arr[i+1]=arr[i]
        print(*arr)
        i-=1
    arr[i+1]=key
    print(*arr)
arr=[1,2,4,5,3]
insertion_sort1(arr)
