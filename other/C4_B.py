x,y,n=map(int, input().split())
grafo={}
for i in range(y):
    a,b=map(int, input().split())
    if a not in grafo:
        grafo[a]=[]
    grafo[a].append(b)
    if b not in grafo:
        grafo[b]=[]
    grafo[b].append(a)
visitados=set()
distancia={}
distancia[n]=0
fila=[n]
while fila:
    atual=fila.pop(0)
    vizinhos=grafo.get(atual)
    visitados.add(atual)
    if atual==1:
        break
    else:
        if vizinhos != None:
            for vizinho in vizinhos:
                if vizinho not in visitados:
                    fila.append(vizinho)
                    distancia[vizinho]=distancia[atual]+1
                    visitados.add(vizinho)
print(distancia[1])