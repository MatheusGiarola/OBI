total=[]
n=int(input())
for i in range(n):
    x=int(input())
    if x==0:
        total.pop()
    else:
        total.append(x)
        t=0
print(sum(total))