s,t,p=map(int, input().split())
altura=[int(x) for x in input().split()]
tuneis={}
for i in range(t):
    x,y=map(int, input().split())
    hx=altura[x-1]
    hy=altura[y-1]
    if hy>hx:
        if y in tuneis:
            tuneis[y].append(x)
        else:
            tuneis[y]=[x]
    else:
        if x in tuneis:
            tuneis[x].append(y)
        else:
            tuneis[x]=[y]
maior=0
visitados=set()
salaoAtual=0
maiorp=0
stack=[p]
while stack:
    salaoAtual=stack[-1]
    possib=tuneis.get(salaoAtual, 0)
    if possib==0:
        stack.pop()
        visitados.add(salaoAtual)
        maiorp-=1
    else:
        verifier=0
        for i in range(len(possib)):
            if possib[i] not in visitados:
                stack.append(possib[i])
                maiorp+=1
                if maiorp>maior:
                    maior=maiorp
                    verifier+=1
                break
        if verifier==0:
            maiorp-=1
            stack.pop()
            visitados.add(salaoAtual)
print(maior)