#Sort the three values and repeatedly move the smallest up by 1 and the largest down by 1 until two values become equal
for _ in range(int(input())):

    a, b, c = map(int, input().split())
    r = 0

    while a != b and b != c and a != c:
        x = min(a, b, c)
        y = max(a, b, c)

        if a == x:
            a += 1
        elif b == x:
            b += 1
        else:
            c += 1

        if a == y:
            a -= 1
        elif b == y:
            b -= 1
        else:
            c -= 1

        r += 1

    print(r)
