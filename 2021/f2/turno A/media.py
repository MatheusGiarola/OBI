a,b=map(int, input().split())
for c in range(-b,b):
    if a<b<c or c<b<a:
        med=b
    elif a<c<b or b<c<a:
        med=c
    else:
        med=a
    if ((a+b+c)/3)==med:
        print(c)
        break
