x = int(input())
y = int(input())
z = int(input())

print((x * y * z) if x != 1 and y and 1 and z != 1 else (max(x, y, z) * (x + y + z - max(x, y, z) ) ))
