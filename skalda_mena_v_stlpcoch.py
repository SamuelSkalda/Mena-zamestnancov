subor = open('mena_zamestnancov.txt','r')
subor1 = open('mena_zamestnancov1.txt','w')
riadky=()
mena=[]
priezviska=[]
nm=''
np=''
cele=[]
for riadok in subor:
    riadky = riadky + (riadok.strip(),)

print('Počet mien v subore je', len(riadky)/2)
for i in range(len(riadky)):
    if i < len(riadky)/2:
        mena.append(riadky[i])
    else:
        priezviska.append(riadky[i])
print(mena)
for i in mena:
    if len(i)>len(nm):
        nm=i   
for i in priezviska:
    if len(i)>len(np):
        np=i
print('Najdlhšie krstné meno je', nm)
print('Najdlhšie priezvisko je', np)
for i in range(len(mena)):
    cele.append(mena[i]+' '+priezviska[i])
    
for meno in cele:
    subor1.write(meno+'\n')
subor.close()
subor1.close()
    
