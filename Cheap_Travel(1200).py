a, b, c, d = map(int, input().split())

plainsum = a * c

n = a // b
m = a - (n * b)

cost = (n * d) + m * c
extra = (n + 1) * d

print(min(plainsum, cost, extra))
