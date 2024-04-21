d=int(input())
a=int(input())
e=int(input())
t=0
if e == 1:
    t=d*(32-e)
elif 1<e<16:
    t=d+a*(e-1)
    t*=(32-e)
else:
    t=d+a*14
    t*=(32-e)
print(t)