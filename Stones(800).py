for _ in range(int(input())):
    a,b,c=map(int,input().split())

    x=min(a,b//2)
    y=min((b-2*x),c//2)

    p=3*(x+y)

    x=min(b,c//2)
    y=min((b-x)//2,a)

    q=3*(x+y)

    print(max(p,q))
