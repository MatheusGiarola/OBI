d=int(input())
n=int(input())
cidades=[]
for i in range(n):
    x=int(input())
    cidades.append(x)
menord=0.0
cidades.sort()
for i in range(n-1):
    aux=0.0
    if i==0:
        aux+=cidades[i]
        aux+=(cidades[i+1]-cidades[i])/2
        menord=aux
    else:
        aux+=(cidades[i]-cidades[i-1])/2
        aux+=(cidades[i+1]-cidades[i])/2
    if aux<menord:
        menord=aux
aux=0.0
aux+=(cidades[n-1]-cidades[n-2])/2
aux+=d-cidades[n-1]

if aux<menord:
    print(f'{aux:.2f}')
else:
    print(f'{menord:.2f}')