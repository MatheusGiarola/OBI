jogo=[[x for x in input().split()] for i in range(7)]
movements=0
horizontaldir='oo.'
horizontalesq='.oo'
for i in range(7):
    line=str(jogo[i])
    movements+=line.count(horizontaldir)
    movements+=line.count(horizontalesq)
    string=''
    for j in range(7):
        line=str(jogo[j])
        string+=line[i]
    movements+=string.count(horizontaldir)
    movements+=string.count(horizontalesq)
print(movements)