n=int(input())
soma=0
for i in range(n):
    x=input()
    lista=[*x]

    p=int(lista[len(lista)-1])
    lista.pop()
    numb=''

    for j in range(len(lista)):
        numb+=lista[j]
    a=(int(numb)**p)        
    soma+=a
print(soma)