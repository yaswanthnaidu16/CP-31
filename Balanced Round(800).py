for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()

    curr = 1
    maxy = 1

    for i in range(1, n):
        if arr[i] - arr[i - 1] <= k:
            curr += 1
        else:
            curr = 1

        maxy = max(maxy, curr)

    print(n - maxy)
