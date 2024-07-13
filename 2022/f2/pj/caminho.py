n=int(input())
postes=[]
for i in range(n):
    x=int(input())
    postes.append(x)
maior=0
acumulado=0
for i in range(n-1):
    pot=postes[i]+postes[i+1]
    if pot<1000:
        acumulado+=1
        if acumulado>maior:
            maior=acumulado
    else:
        acumulado=0
if postes[0]+postes[n-1]<1000:
    maior+=1
print(maior)