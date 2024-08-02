jogadores=list(map(int,input().split()))
k=jogadores.index(1)+1
l=jogadores.index(9)+1
if k+1==l or l+1==k:
    print('oitavas')
elif 1<=k<=4 and 5<=l<=8 or 1<=l<=4 and 5<=k<=8:
    print('semifinal')
elif 9<=k<=12 and 13<=l<=16 or 9<=l<=12 and 13<=k<=16:
    print('semifinal')
elif 1<=k<=8 and 9<=l<=16 or 1<=l<=8 and 9<=k<=16:
    print('final')
else:
    print('quartas')