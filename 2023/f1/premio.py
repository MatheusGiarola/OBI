p=int(input())
d=int(input())
b=int(input())

totalV= p + d*2 + b*3

if totalV>=150:
    print('B')
elif totalV>=120:
    print('D')
elif totalV>=100:
    print('P')
else:
    print('N')