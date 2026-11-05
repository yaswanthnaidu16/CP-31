s = input()

maxy0 = 0
maxy1 = 0
curr0 = 0
curr1 = 0

for i in s:
    if i == '0':
        curr0 += 1
        curr1 = 0
        maxy0 = max(maxy0, curr0)
        
    else:
        curr1 += 1
        curr0 = 0
        maxy1 = max(maxy1, curr1)
        
if maxy0 >= 7 or maxy1 >= 7:
    print("YES")
else:
    print("NO")
