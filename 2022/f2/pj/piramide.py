n=int(input())
matriz=[[0 for i in range(n)] for i in range(n)]
inc=1
pos=0
def oddeven(n):
    if n%2==0:
        return n/2
    else:
        return(n//2+1)
rang=int(oddeven(n))
while pos<(rang):
    for i in range(rang):
        for j in range(rang):
            matriz[i][pos]=inc
            matriz[pos][j]=inc
            matriz[i][(n-1-pos)]=inc
            matriz[(n-1-pos)][j]=inc
        pos+=1
        inc+=1
print(matriz)