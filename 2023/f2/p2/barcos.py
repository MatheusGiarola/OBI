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

c=int(input())
for _ in range(c):
    o,d=map(int, input().split())

    mPassageiros=[]
    ilhasVisitadas=[]
    queue=barcos.get(o)
    while queue:
        size=len(queue)
        ilhaAtual=queue[-1]

        if ilhaAtual[0]==d:
            mPassageiros.append(ilhaAtual[1])
            queue.pop()
        else:
            if ilhaAtual not in ilhasVisitadas:
                npassageiros=ilhaAtual[1]
                proximas=barcos.get(ilhaAtual[0])
                ilhasVisitadas.append(ilhaAtual[0])

                length=len(proximas)
                queue.pop()
                for x in range(length):
                    if x not in ilhasVisitadas:
                        proximas[x][1]=min(npassageiros,proximas[x][1])
                        queue.append(proximas[x]) 
            else:
                queue.pop()
    maximo=0
    for z in mPassageiros:
        if z>maximo:
            maximo=z
    print(maximo)