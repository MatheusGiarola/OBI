n=int(input())
dp=[0]*(n+1)
def path(n):
    possibs=str(n)
    tam=len(possibs)
    if dp[n]!=0:
        return dp[n]
    else:
        if tam==1:
            if possibs!='0':
                dp[n]=1
            else:
                dp[n]=0
        else:
            menor=float('inf')
            for i in possibs:
                if i !='0':
                    num=n-int(i)
                    if dp[num]==0:
                        dp[num]=path(num)
                    menor=min(menor,dp[num])
            dp[n]=1+menor
    return dp[n]
value=path(n)
print(value)