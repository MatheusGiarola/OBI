n,c,s=map(int,input().split())
comandos=[int(x) for x in input().split()]
estaçãoAtual=1
count=0
if estaçãoAtual==s:
        count+=1
for i in range(c):
    if comandos[i]<0:
        if estaçãoAtual==1:
            estaçãoAtual=n
        else:
            estaçãoAtual-=1
    else:
        if estaçãoAtual==n:
            estaçãoAtual=1
        else:
            estaçãoAtual+=1
    if estaçãoAtual==s:
        count+=1
print(count)