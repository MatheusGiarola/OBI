n,a,b=map(int, input().split())
linhas={}
for i in range(n-1):
    x,y=map(int, input().split())
    if x not in linhas:
        linhas[x]=[]
    linhas[x].append(y)
    if y not in linhas:
        linhas[y]=[]
    linhas[y].append(x)
distancias={}
distancias[a]=0
visitados=set()
fila=[a]
while fila:
    atual=fila.pop(0)
    visitados.add(atual)
    if atual ==b:
        break
    else:
        vizinhas=linhas.get(atual)
        if vizinhas != None:
            for vizinho in vizinhas:
                if vizinho not in visitados:
                    fila.append(vizinho)
                    visitados.add(vizinho)
                    distancias[vizinho]=distancias[atual]+1
print(distancias[b])