q=int(input())
n=int(input())
tm=q*(n+1)
for i in range(n):
    u=int(input())
    tm-=u
print(tm)