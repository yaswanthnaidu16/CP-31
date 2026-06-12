s = list(input())

for i in range(len(s)):
    d = int(s[i])

    if i == 0:
        if d > 4 and d != 9:
            s[i] = str(9 - d)
    else:
        if d > 4:
            s[i] = str(9 - d)

print("".join(s))
