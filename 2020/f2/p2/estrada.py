t=int(input())
n=int(input())
cidades=[]
for i in range(n):
    cidades.append(float(input()))
cidades.sort()
menorV=0.0
for i in range(n-1):
    if i==0:
        esquerda=cidades[i]
        direita=(cidades[i+1]-cidades[i])/2
        menorV=esquerda+direita
    else:
        esquerda=(cidades[i]-cidades[i-1])/2
        direita=(cidades[i+1]-cidades[i])/2
        aux=esquerda+direita
        if aux<menorV:
            menorV=aux
last=((cidades[n-1]-cidades[n-2])/2)+(t-cidades[n-1])
if last<menorV:
    menorV=last
print(f'{menorV:.2f}')