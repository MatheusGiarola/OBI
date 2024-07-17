k=int(input())
l=int(input())

if 1<=l<=8 and 9<=k<=16:
    print('final')
elif 1<=k<=8 and 9<=l<=16:
    print('final')
elif 1<=l<=4 and 5<=k<=8:
    print('semifinal')
elif 1<=k<=4 and 5<=l<=8:
    print('semifinal')
elif 9<=l<=12 and 13<=k<=16:
    print('semifinal')
elif 9<=k<=12 and 13<=l<=16:
    print('semifinal')
elif (k-1)==l:
    print('oitavas')
elif (l-1)==k:
    print('oitavas')
else:
    print('quartas')