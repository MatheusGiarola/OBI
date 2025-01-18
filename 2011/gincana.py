n,m=map(int, input().split())
grafo={}
visited=set()
possibs=0
for i in range(m):
    x,y=map(int, input().split())
    if x in grafo:
        grafo[x].append(y)
    else:
        grafo[x]=[y]
    if y in grafo:
        grafo[y].append(x)
    else:
        grafo[y]=[x]
for i in range(1,n+1):
    if i not in visited:
        group=1
        queue=[i]
        while queue:
            atual=queue.pop(0)
            friends=grafo.get(atual, None)
            if friends!=None:
                for j in friends:
                    if j not in visited:
                        group+=1
                        queue.append(j)
            visited.add(atual)
        possibs+=1
print(possibs)