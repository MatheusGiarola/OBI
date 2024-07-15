r=int(input()) #resultado atleta
m=int(input()) #recorde mundial
l=int(input()) #recorde olimpico
if r<m:
    print('RM')
else:
    print('*')
if r<l:
    print('RO')
else:
    print('*')