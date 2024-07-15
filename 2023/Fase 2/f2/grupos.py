e,m,d=[int(x) for x in input().split()]
dicionariom={}
dicionariod={}
violacoes=0
for i in range(m):
    x,y=map(int, input().split())
    dicionariom[x]= y

for i in range(d):
    x,y=map(int, input().split())
    dicionariod[x]= y

for i in range(int(e/3)):
    grupo=[int(x) for x in input().split()]
    for i in range(3):
        aux=dicionariom.get(grupo[i], 0)
        if aux!=0:
            if aux not in grupo:
                violacoes+=1

        aux=dicionariod.get(grupo[i], 0)
        if aux!=0:
            if aux in grupo:
                violacoes+=1
print(violacoes)