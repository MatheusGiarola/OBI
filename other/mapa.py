l,c=map(int, input().split())
mapa=[]
inicial=()
for i in range(l):
    aux=input()
    x=[*aux]
    if 'o' in x:
        coluna=x.index('o')
        inicial=(i,coluna)
    mapa.append(x)
queue=[inicial]
visitados=set()
while queue:
    atual=queue.pop(0)
    linha=atual[0]
    coluna=atual[1]
    pos=[(-1,0),(1,0),(0,-1),(0,1)]
    for v in pos:
        novaLinha=linha+v[0]
        novaColuna=coluna+v[1]
        if 0<=novaLinha<l and 0<=novaColuna<c:
            if mapa[novaLinha][novaColuna]=='H':
                posicaoA=(novaLinha,novaColuna)
                if posicaoA not in visitados:
                    queue.append(posicaoA)
                    visitados.add(posicaoA)
print(f'{atual[0]+1} {atual[1]+1}')
