tam=[int(x) for x in input().split()]
tam.sort()
n=int(input())
melhorm=-1
tam1=101
tam2=101
for i in range(n):
    medidas=[int(x) for x in input().split()]
    medidas.sort()
    if medidas[0]>=tam[0] and medidas[1]>=tam[1]:
        aream=medidas[0]*medidas[1]
        areamenor=tam1*tam2
        if aream<areamenor:
            melhorm=i+1
            tam1=medidas[0]
            tam2=medidas[1]
print(melhorm)