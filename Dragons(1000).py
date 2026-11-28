a, b = map(int, input().split())

l = []

for i in range(b):
    x, y = map(int, input().split())
    l.append([x, y])

l.sort()

for i in range(b):
    if a > l[i][0]:
        a += l[i][1]
    else:
        print("NO")
        break
else:
    print("YES")
