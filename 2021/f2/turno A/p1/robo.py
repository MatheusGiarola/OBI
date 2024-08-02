n,c,s=map(int, input().split())
estacaoatual=1
vezes=0
comandos=[int(x) for x in input().split()]
for i in comandos:
    if estacaoatual==s:
        vezes+=1
    if i==-1 and estacaoatual==1:
        estacaoatual=n
    elif i==1 and estacaoatual==n:
        estacaoatual=1
    else:
        estacaoatual+=i
if estacaoatual==s:
        vezes+=1
print(vezes)