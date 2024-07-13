t=0
for i in range(2):
    x=int(input())
    if x<=17:
        t+=15
    elif 17<x<=60:
        t+=30
    else:
        t+=20
print(t)