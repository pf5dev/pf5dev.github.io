import os
os.system('clear')
a=[['1234','abc:algumacoisa'],['5678','def:outracoisa'],['9101112','ghi:aindaoutracoisa']]
for i in range(len(a)):
    a1,a2=a[i]
    if a[i][1]==a2:
        print(f'{a2}')       
