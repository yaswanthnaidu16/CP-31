#Find the minimum number of initial water placements needed to fill all empty cells using spreading and water movement operations
for _ in range(int(input())):
    n = int(input())
    s = input()

    mx = 0
    cnt = 0
    dots = s.count('.')

    for ch in s:
        if ch == '.':
            cnt += 1
            mx = max(mx, cnt)
        else:
            cnt = 0

    if mx >= 3:
        print(2)
    else:
        print(dots)
