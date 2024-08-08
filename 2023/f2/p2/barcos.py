n,b=map(int, input().split())
grafo={} #{1: {4: 50, 5: 85, 3: 40}, 4: {1: 50, 2: 80, 5: 75}, 5: {1: 85, 4: 75}, 2: {3: 60, 4: 80}, 3: {2: 60, 1: 40}}
for i in range(6):
    x,y,c=map(int, input().split())
    if x not in grafo:
        grafo[x]={}
    grafo[x][y]=c
    if y not in grafo:
        grafo[y]={}
    grafo[y][x]=c
ilhas=[float('inf') for _ in range(n)] 
c=int(input())
for i in range(c):
    x,y=map(int, input().split())
    visitados=set()
    fila=[x]
    while fila:
        atual=fila.pop(0)
        visitados.add(atual)
        vizinhos=grafo.get(atual)
        if vizinhos != None:
            capacidades=[]
            for vizinho in vizinhos:
                if vizinho not in visitados:
                    fila.append(vizinho)
                    visitados.add(vizinho)
                
                ilhas[vizinho-1]=min(ilhas[atual-1],grafo[atual][vizinho])
    print(ilhas[y-1])