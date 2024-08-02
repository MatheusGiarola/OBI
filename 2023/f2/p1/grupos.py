e,m,d=map(int, input().split())
dictm={}
dictd={}
violacoes=0
for i in range(m):
    x,y=map(int, input().split())
    dictm[x]=y
for i in range(d):
    x,y=map(int, input().split())
    dictd[x]=y
for i in range(e//3):
    grupo=[int(x) for x in input().split()]
    for j in range(3):
        x=dictm.get(grupo[j], 0)
        if x!=0:
            if x not in grupo:
                violacoes+=1
        
        x=dictd.get(grupo[j], 0)
        if x!=0:
            if x in grupo:
                violacoes+=1
print(violacoes)