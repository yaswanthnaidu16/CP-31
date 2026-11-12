s = input()
target = "hello"

j = 0

for c in s:
    if c == target[j]:
        j += 1
        
        if j == 5:
            break
        
print("YES" if j == 5 else "NO")
