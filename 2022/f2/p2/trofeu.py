alunos=[]
for i in range(5):
    x=int(input())
    alunos.append(x)
trofeu=alunos.count(alunos[0])
maior2=101
for i in range(5):
    if alunos[i] != alunos[0]:
        maior2=alunos[i]
        break
medalhas=alunos.count(maior2)
print(f'{trofeu} {medalhas}')