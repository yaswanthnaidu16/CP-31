#Find the missing team efficiency such that the sum of efficiencies of all teams becomes zero

for _ in range(int(input())):
    a = int(input())
    x = list(map(int, input().split()))

    sumy = sum(x)

    if sumy > 0:
        print(-sumy)
    else:
        print(abs(sumy))
