b=int(input())
t=int(input())
areaMetade=(160*70)/2
pFelix=((b+t)*70)/2
if pFelix == areaMetade:
    print(0)
elif pFelix > areaMetade:
    print(1)
else:
    print(2)