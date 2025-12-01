def strange_counter(n):
    start=3
    while n>start:
        n-=start
        start*=2
    return start+n-1
n=4
print(strange_counter(n))
