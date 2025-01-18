n,r=map(int, input().split())
for i in range(r):
    x,y=map(int, input().split())
relacionamentos=(n*(n-1))/2
relacionamentos-=r
print(int(relacionamentos))