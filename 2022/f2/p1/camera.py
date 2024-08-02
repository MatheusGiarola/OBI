m,n,k=map(int, input().split()) #coluna, linha, câmeras
matriz=[[0 for i in range(m)]for i in range(n)]
for i in range(k):
    c,l,d=input().split()
    c=int(c)-1
    l=int(l)-1
    aux=0
    if d=='N':
        aux=l
        while aux>=0:
            matriz[aux][c]=1
            aux-=1
    elif d=='S':
        aux=l
        while aux<=(n-1):
            matriz[aux][c]=1
            aux+=1
    elif d=='O':
        aux=c
        while aux>=0:
            matriz[l][aux]=1
            aux-=1
    else:
        aux=c
        while aux<=(m-1):
            matriz[l][aux]=1
            aux+=1
for i in range(n):
    print(matriz[i])