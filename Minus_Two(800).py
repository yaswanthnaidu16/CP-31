for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    odd = 0
    even0 = 0
    even2 = 0

    for i in a:
        if i % 2 != 0:
            odd += 1
        elif i % 4 == 0:
            even0 += 1
        else:
            even2 += 1

    print(max(odd, even0, even2))
