n,m=map(int, input().split())
rest={}
for i in range(m):
    x,y=map(int,input().split())
    if x not in rest:
        rest[x]=[]
    rest[x].append(y)

possib=set()
for i in range(n):
    possib.add((i,))
q=2
anterior=list(possib)
while q<n:
    qpossibs=[]
    for c in range(len(anterior)):
        for i in range(n):
            atual=list(anterior[c])
            atual.append(i) # formou nova possibilidade
            infracao=False
            mesmo=False
            for j in range(len(atual)):
                aux=rest.get(atual[j]+1)
                if aux!=None:
                    for item in aux:
                        if (item-1) in atual:
                            infracao=True
                            break
                if infracao:
                    break
            for ingr in atual:
                if atual.count(ingr)>1:
                    mesmo=True
            if not mesmo and not infracao:
                atual.sort()
                combinacao=tuple(atual)
                if combinacao not in qpossibs:
                    qpossibs.append(combinacao)
                    print(combinacao)
    for i in qpossibs:
        possib.add(i)
    anterior=qpossibs
    q+=1
if m==0:
    print(len(possib)+1)
else:
    print(len(possib))