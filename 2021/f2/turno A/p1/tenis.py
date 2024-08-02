amigos=[]
for i in range(4):
    x=int(input())
    amigos.append(x)
amigos.sort()
diferenca=abs((amigos[0]+amigos[3])-(amigos[1]+amigos[2]))
print(diferenca)