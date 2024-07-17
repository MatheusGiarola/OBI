n=int(input())
m=int(input())
figs=[]
valFigs=m
for i in range(m):
    x=int(input())
    figs.append(x)
for i in range(n+1):
    x=figs.count(i)
    if x>=2:
        valFigs-=(x-1)
figsToGo=n-valFigs
print(figsToGo)
