n = int(input())
x = list(map(int, input().split()))

curr = 0
maxy = 0

for i in range(1, n):
    if x[i] >= x[i-1]:
        curr += 1
        maxy = max(curr, maxy)
        
    else:
        curr = 0
        
print(maxy + 1)
