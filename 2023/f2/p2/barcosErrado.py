n,b=map(int, input().split())
barcos={}
for a in range(b):
    i,j,p=map(int, input().split())
    if i in barcos:
        barcos[i].append([j,p])
    else:
        barcos[i]=[[j,p]]
    if j in barcos:
        barcos[j].append([i,p])
    else:
        barcos[j]=[[i,p]]

def caminho(ilha,qPassageiros):
    if ilha==d:
            return qPassageiros
    else:
        possib=barcos.get(ilhaAtual)

        for i in range(len(possib)):
            destino=possib[i][0]
            qPassageiros=min(possib[i][1], qPassageiros)
            caminho(destino,qPassageiros)

c=int(input())
maiorq=0
for _ in range(c):
    o,d=map(int, input().split())
    ilhaAtual=o

    possibs=barcos.get(ilhaAtual)
    for i in range(len(possibs)):
        if possibs[i][0]==d:
            if possibs[i][1]>maiorq:
                maiorq=possibs[i][1]
    trajetos=[]
    for i in range(len(possibs)):
        x=caminho(possibs[i][0],possibs[i][1])
        trajetos.append(x)
    maiorq=max(trajetos,maiorq)
    print(maiorq)