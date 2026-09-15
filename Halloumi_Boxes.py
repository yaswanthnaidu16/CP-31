for _ in range(int(input())):
    a, b = map(int, input().split())
    x = list(map(int, input().split()))

    if b == 1:
        if x == sorted(x):
            print("YES")
        else:
            print("NO")
            
    else:
        print("YES")
