h=input()
v=input()
ih=0
iv=0
verifier=0
for i in h:
    for j in v:
        if i==j:
            ih=(h.index(i)+1)
            iv=(v.index(j)+1)
            verifier+=1
            print(f'{ih} {iv}')
            break
if verifier==0:
    print(f'{-1} {-1}')