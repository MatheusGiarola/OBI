s,t,p=map(int, input().split())
alturas=list(map(int, input().split()))
caminhos={}
profundidade=0
maiorProfundidade=0
for i in range(t):
    i,j=map(int, input().split())
    if alturas[i-1]>alturas[j-1]:
        maior=i
        menor=j
    else:
        maior=j
        menor=i
    if maior not in caminhos:
        caminhos[maior]=[]
    caminhos[maior].append(menor)
visitados=set()

def dfs(salao,depth,maiorP):
    vizinhos=caminhos.get(salao)
    visitados.add(salao)
    if vizinhos==None:
        if depth>maiorP:
            maiorP=depth
        depth-=1
        return maiorP
    else:
        depth+=1
        for vizinho in vizinhos:
            if vizinho not in visitados:
                maiorP=dfs(vizinho, depth, maiorP)  
            return maiorP
        
maiorProfundidade=dfs(p,profundidade,maiorProfundidade)
print(maiorProfundidade)