s,t,p=map(int, input().split())
alturas=[int(x) for x in input().split()]
tuneis={}
for i in range(t):
    x,y=map(int, input().split())
    hx=alturas[x-1]
    hy=alturas[y-1]
    if hx>hy:
        if x in tuneis:
            tuneis[x].append(y)
        else:
            tuneis[x]=[y]
    else:
        if y in tuneis:
            tuneis[y].append(x)
        else:
            tuneis[y]=[x]
visitados=set()
stack=[p]
maior=0
profundidade=0
while stack:
    atual=stack[-1]
    possib=tuneis.get(atual,0)
    if possib==0:
        stack.pop()
        profundidade-=1
        visitados.add(atual)
    else:
        verifier=0
        for i in range(len(possib)):
            if possib[i] not in visitados:
                stack.append(possib[i])
                profundidade+=1
                if profundidade>maior:
                    maior=profundidade
                verifier+=1
                break
        if verifier==0:
            profundidade-=1
            stack.pop()
            visitados.add(atual)
print(maior)