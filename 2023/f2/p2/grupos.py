e,m,d=map(int, input().split())
mesmogp={}
gpdiferente={}
violacoes=0
for i in range(m):
    x,y=map(int, input().split())
    mesmogp[x]=y
for j in range(d):
    x,y=map(int, input().split())
    gpdiferente[x]=y
for i in range(e//3):
    grupo=[int(x) for x in input().split()]
    for j in grupo:
        junto=mesmogp.get(j,0)
        separado=gpdiferente.get(j,0)
        if junto not in grupo and junto !=0:
            violacoes+=1
        if separado in grupo and separado !=0:
            violacoes+=1
print(violacoes)