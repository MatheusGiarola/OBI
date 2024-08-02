n=int(input())
numeros=[]
for i in range(n):
    numeros.append(int(input()))
maior=0
aux=[]
for i in numeros:
    if i not in aux:
        aux.append(i)
    else:
        if len(aux)>maior:
            maior=len(aux)
        x=aux.index(i)
        for j in range(x+1):
            aux.pop(0)
        aux.append(i)
if len(aux)>maior:
    maior=len(aux)
print(maior)