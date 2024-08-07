n,m,k=map(int, input().split()) #coluna, linha
matriz=[[0 for _ in range(n)] for w in range(m)]
for i in range(k):
    c,l,d=input().split()
    c=int(c)
    l=int(l)
    c-=1
    l-=1
    if d=='N':
        while l>=0:
            matriz[l][c]=1
            l-=1
    elif d=='S':
        while l<=(m-1):
            matriz[l][c]=1
            l+=1
    elif d=='O':
        while c>=0:
            matriz[l][c]=1
            c-=1
    else:
        while c<=(n-1):
            matriz[l][c]=1
            c+=1

def norte(cell):
    x,y=cell
    if x-1<0 or matriz[x][y]==1:
        return None
    else:
        linha=x-1
        coluna=y
        return (linha,coluna)
    
def sul(cell):
    x,y=cell
    if x+1==m or matriz[x][y]==1:
        return None
    else:
        linha=x+1
        coluna=y
        return (linha,coluna)

def leste(cell):
    x,y=cell
    if y+1==n or matriz[x][y]==1:
        return None
    else:
        linha=x
        coluna=y+1
        return (linha,coluna)

def oeste(cell):
    x,y=cell
    if y-1<0 or matriz[x][y]==1:
        return None
    else:
        linha=x
        coluna=y-1
        return (linha,coluna)

chegou=False
if matriz[0][0]==1 or matriz[m-1][n-1]==1:
    print('N')
else:
    atual=(0,0)
    visitados=set()
    stack=[atual]
    while stack:
        atual=stack[-1]
        if atual==(m-1,n-1):
            print('S')
            chegou=True
            break
        else:
            possib=[]
            if norte(atual) != None:
                possib.append(norte(atual))
            if oeste(atual) != None:
                possib.append(oeste(atual))
            if sul(atual) != None:
                possib.append(sul(atual))
            if leste(atual) != None:
                possib.append(leste(atual))
            if possib==[]:
                visitados.add(atual)
                stack.pop()
            else:
                for i in possib:
                    if i not in visitados:
                        stack.append(i)
                visitados.add(atual)
if not chegou:
    print('N')