n=int(input())
hPredios=[int(x) for x in input().split()]
distanciaMax=0
aux=0

for i in range(n):
    for j in range(n):
        aux=(hPredios[i])+(hPredios[j])+abs(i-j)
        if aux> distanciaMax:
            distanciaMax=aux
print(distanciaMax)
