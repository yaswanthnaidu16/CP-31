n = int(input())
x = list(map(int, input().split()))

ans = 0
curr = 0
summy = sum(x)
x.sort(reverse = True)

for i in x:
    curr += i
    summy -= i
    ans += 1
    curr > summy:
        break
    
print(ans)
