n=int(input())
matriz=[[1 for i in range(n)]for i in range(n)]
def height(x):
    if x%2==0:
        return x//2
    else:
        return(x//2)+1
h=height(n)
count=n
start=0
for k in range(h-1):
    for i in range(start,count-2):
        for j in range(start,count-2):
            matriz[i+1][j+1]+=1
    count-=1
    start+=1
for i in range(n):
    print(" ".join(map(str, matriz[i])))
