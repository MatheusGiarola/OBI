n=int(input())
matriz=[[0 for i in range(n)] for i in range(n)]
start=0
stop=n
if n%2==0:
    h=int(n/2)
else:
    h=int((n/2)+1)
for i in range(h):
    for i in range(start,stop):
        for j in range(start,stop):
            matriz[i][j]+=1
    start+=1
    stop-=1
for i in range(n):
    print(" ".join(map(str, matriz[i])))