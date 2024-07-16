j,p,v,e,d=map(int, input().split())

if e==-1:
    e=p-(3*v)
if p==-1:
    p=(3*v)+e
if j==-1:
    j=v+e+d
if v==-1:
    v=j-e-d
if d==-1:
    d=j-v-e
print(f'{j} {p} {v} {e} {d}')