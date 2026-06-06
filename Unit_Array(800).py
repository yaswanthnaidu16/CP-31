for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))

    summy = sum(x)

    product = 1
    for i in x:
        product *= i

    ans = 0

    while summy < 0:
        summy += 2      
        product *= -1   
        ans += 1
    if product == -1:
        ans += 1

    print(ans)
