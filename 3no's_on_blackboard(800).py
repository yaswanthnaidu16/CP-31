#If the largest number is greater than the sum of the other two, replace it with their sum; otherwise, keep the original numbers, and calculate the minimum range.
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    maxy = max(a, b, c)
    if (maxy > a + b) or (maxy > b + c) or (maxy > a + c):
        print((a+b+c-maxy) - min(a, b, c))
    else:
        print(maxy - min(a, b, c))
