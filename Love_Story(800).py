for _ in range(int(input())):
    s = input()
    ref = "codeforces"
    count = 0

    for i in range(len(s)):
        if s[i] != ref[i]:
            count += 1

    print(count)
