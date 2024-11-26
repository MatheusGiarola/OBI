n,m,k=map(int, input().split())
senha=input()
possibs=[]
for _ in range(m):
    pal=input()
    if possibs ==[]:
        indice=senha.index('#')
        aux=[*senha]
        for i in pal:
            aux[indice]=i
            concat="".join(aux)
            possibs.append(concat)
        print(possibs)
    else:
        for i in possibs:
            options=[]
            atual=possibs[0]
            aux=[*atual]
            if aux.count('#')!=0:
                possibs.pop(0)
                indice=aux.index('#')
                for l in pal:
                    aux[indice]=l
                    print(aux)
                    concat="".join(aux)
                    options.append(concat)
                possibs.extend(options)
            else:
                break
p=int(input())
ordenado=sorted(possibs)
print(possibs)
print(ordenado)
print(possibs[p-1])