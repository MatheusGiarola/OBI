n,f=map(int, input().split())
dias=0
ciclos=list(map(int, input().split()))
nmoedas=0
while nmoedas<f:
    dias+=1
    nmoedas=0
    for i in range(n):
        nmoedas+=dias//ciclos[i]
print(dias)