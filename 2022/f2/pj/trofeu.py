alunos=[]
for i in range(5):
    x=int(input())
    alunos.append(x)
trofeu=1
placa=0
maior=alunos[0]
for i in range(4):
    if maior==alunos[i+1]:
        trofeu+=1
    maior2=alunos[(-5+trofeu)]
    if maior2==alunos[i+1] and maior2<maior:
        placa+=1
print(f'{trofeu} {placa}')