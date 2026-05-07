#If n is divisible by 3, Vova wins otherwise Vanya makes it divisible by 3 in one move and wins.

for _ in range(int(input())):
    n = int(input())

    if n % 3 == 0:
        print("Second")
    else:
        print("First")
