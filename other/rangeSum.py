lista=[int(x) for x in input().split()]
n=int(input())
left=int(input())
right=int(input())
sub=[]
mod=10**9+7
dp=[[] for _ in range(n)]
dp[0].append(lista[0])
sub.append(lista[0])
for i in range(1,n):
    valor=lista[i]
    for k in dp[i-1]:
        substring=k+valor
        dp[i].append(substring)
        sub.append(substring)
    dp[i].append(lista[i])
    sub.append(lista[i])
sub.sort()
intervalo=sub[left-1:right]
soma=0
for i in intervalo:
    soma+=i
print(soma%mod)