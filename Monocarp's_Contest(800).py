for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))

    c0 = x.count(0)

    if c0 < 2:
        print(-1)
    elif x[0] == 0 and x[-1] == 0:
        print(0)
    elif x[0] == 0 or x[-1] == 0:
        print(1)
    else:
        print(2)
