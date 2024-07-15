alunos=int(input())
grande=int(input())
pequena=int(input())
total=grande*8+pequena*6
total-=alunos
if total<=0:
    print(0)
else:
    print(total)