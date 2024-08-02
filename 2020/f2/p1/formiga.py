s,t,p=map(int, input().split())
alturas=list(map(int,input().split()))
saloes={}
for i in range(t):
    x,y=map(int, input().split())
    if x in saloes:
        saloes[x].append(y)
    else:
        saloes[x]=[y]
    if y in saloes:
        saloes[y].append(x)
    else:
        saloes[y]=[x]

possibilidades=0

sConectados=saloes[p]
hp=alturas[p-1]
for i in sConectados:
     hi=alturas[i-1]
     if hp>hi:
         possibilidades+=1
print(possibilidades)
