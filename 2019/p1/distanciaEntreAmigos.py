n=int(input())
hPredios=[]
distanciaMax=0
aux=0

for i in range(n):
    x=int(input())
    hPredios.append(x)

for i in range(hPredios):
    for j in range(hPredios-i):
        aux=(hPredios[i]+1)+(hPredios[j]+1)+abs(hPredios.index(hPredios[i])-hPredios.index(hPredios[j]))
        if aux> distanciaMax:
            distanciaMax=aux
print(distanciaMax)