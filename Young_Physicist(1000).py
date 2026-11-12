sx, sy, sz = 0, 0, 0
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    sx += a
    sy += b
    sz += c
if sx == 0 and sy == 0 and sz == 0:
    print("YES")
else:
    print("NO")
