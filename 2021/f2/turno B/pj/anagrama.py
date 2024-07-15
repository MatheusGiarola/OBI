n=int(input())
stringa=input()
stringb=input()
dicta={}
dictb={}

for i in stringa:
    if i in dicta:
        dicta[i]+=1
    else:
        dicta[i]=1

for i in stringb:
    if i in dictb:
        dictb[i]+=1
    else:
        dictb[i]=1

verifier=0
for i in stringa:
    if i not in stringb:
        print('N')
        break
    else:
        if i==' ' or i=='.' or i==',':
            pass
        else:
            if dicta[i]!=dictb[i]:
                print('N')
                break
            else:
                verifier+=1
if verifier>0:
    print('S')