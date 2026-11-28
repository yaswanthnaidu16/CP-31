s = input()

if s.isupper() or s[1:].isupper():
    if s[0].isupper():
        print(s.lower())
    else:
        print(s.capitalize())
else:
    print(s)
