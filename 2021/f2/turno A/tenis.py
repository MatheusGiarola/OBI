amigos=[]
for i in range(4):
    x=int(input())
    amigos.append(x)
amigos.sort()
a=amigos[0]+amigos[3]
b=amigos[1]+amigos[2]
dif=abs(a-b)
print(dif)