#If cheese <= sausage, print -1 otherwise print min of sausage slices and excess slices
for _ in range(int(input())):
    a, b = map(int, input().split())

    if a <= b:
        print(-1)
    else:
        print(min(b, a - b))
