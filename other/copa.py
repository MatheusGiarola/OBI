def preco(n:list):
    return n[0]
n,f,r=map(int, input().split())
caminhosF=[]
caminhosR=[]
for _ in range(f):
    a,b,c=map(int, input().split())
    caminhosF.append([c,a,b])
caminhosFOrd=sorted(caminhosF,key=preco)

for _ in range(r):
    a,b,c=map(int, input().split())
    caminhosR.append([c,a,b])
caminhosROrd=sorted(caminhosR,key=preco)
visitados=set()
custo=0
pos=0
arestas=0
while arestas<(n-1) and pos<f:
    c=caminhosFOrd[pos][0]
    a=caminhosFOrd[pos][1]
    b=caminhosFOrd[pos][2]
    if a in visitados and b in visitados:
        pass
    else:
        custo+=c
        visitados.add(a)
        visitados.add(b)
        arestas+=1
    pos+=1
    print(arestas,'f')

pos=0
while arestas<(n-1) and pos<r:
    c=caminhosROrd[pos][0]
    a=caminhosROrd[pos][1]
    b=caminhosROrd[pos][2]
    if a in visitados and b in visitados:
        custo+=c
        visitados.add(a)
        visitados.add(b)
        arestas+=1
    else:
        custo+=c
        visitados.add(a)
        visitados.add(b)
        arestas+=1
    pos+=1
    print(arestas,'r')
print(custo)