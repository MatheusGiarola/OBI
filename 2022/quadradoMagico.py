n=int(input())
cubo=[]
linhaC=0
colunaC=0
valor=0
aux=0

for i in range(n):
    linha=[int(x) for x in input().split()]
    cubo.append(linha)

for i in range(n):
    for j in range(n):
        if cubo[i][j] ==0:
            linhaC=i
            colunaC=j

for i in range(n):
    aux+=cubo[linhaC][i] #aux=sum(cubo[linhaC])

if linhaC == 0:
    for i in range(n):
        valor+=cubo[1][i] #valor=sum(cubo[1])
else:
    for i in range(n):
        valor+=cubo[0][i] #valor=sum(cubo[0])
valor-=aux
print(valor)
print(linhaC+1)
print(colunaC+1)