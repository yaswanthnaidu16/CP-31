#Count the number of `1`s and `0`s if `1`s are greater than or equal to `0`s, Bessie wins, otherwise Elsie wins.
for _ in range(int(input())):
    a = int(input())
    x = list(map(int, input().split()))
    o = x.count(1)
    z = x.count(0)
    if o >= z:
        print("Bessie")
    else:
        print("Elsie")
