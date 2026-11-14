n = int(input())

lucky = []

for i in range(1, n + 1):
    if all(ch in "47" for ch in str(i)):
        lucky.append(i)

if any(n % d == 0 for d in lucky):
    print("YES")
else:
    print("NO")
