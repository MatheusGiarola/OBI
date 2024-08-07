n=int(input())
valores=[]
for i in range(n):
    x=int(input())
    valores.append(x)
maior=0
intervalo=[]
for i in valores:
    if i not in intervalo:
        intervalo.append(i)
    else:
        if len(intervalo)>maior:
            maior=len(intervalo)
        rep=intervalo.index(i)
        for j in range(rep+1):
            intervalo.pop(0)
        intervalo.append(i)
if len(intervalo)>maior:
    maior=len(intervalo)
print(maior)