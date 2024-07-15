nDeChinelos=int(input())
chinelos=[]
pedidosEfetivados=0

for i in range(nDeChinelos):
    x=int(input())
    chinelos.append(x)

nDePedidos=int(input())
for i in range(nDePedidos):
    x=int(input())
    if chinelos[(x-1)]>0:
        pedidosEfetivados+=1
        chinelos[(x-1)]-=1
print(pedidosEfetivados)