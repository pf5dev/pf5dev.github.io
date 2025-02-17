import os
import os.path
import glob
import pandas as pd
import random
from abc import ABC, abstractmethod
os.system('cls')
os.chdir(os.path.expandvars(r'c:%HOMEPATH%'))
f0=glob.glob('*.xlsx')
df0=pd.read_excel(f'{f0[0]}',sheet_name='Acessos')
l0=df0['Título do Chamado'].tolist()
df1=pd.read_excel(f'{f0[0]}',sheet_name='E-mail')
l1=df1['Título do Chamado'].tolist()
df2=pd.read_excel(f'{f0[0]}',sheet_name='Pastas')
l2=df2['Título do Chamado'].tolist()
df3=pd.read_excel(f'{f0[0]}',sheet_name='BC')
l3=df3['BC'].tolist()
l4=sorted(l0+l1+l2+l3)
lx=list(enumerate(l4))
print(lx)
# os.chdir(os.path.expandvars(r'c:%HOMEPATH%\Downloads'))
# f1=glob.glob('*.csv')
# ###############################################################################
# class Base(ABC):
#     def __init__(self,*args):
#         self.s0=None
#         self.s1=None
#         self.s2=None
            
#     @abstractmethod
#     def pwdgen(self):
#         pass
        
# class Label(Base):
#     def __init__(self,*args):
#         super().__init__(*args)
#         self.s03='Usuário: | '
#         self.s04='Usuário: | Senha: 12345678'
   
#     def pwdgen(self):
#         u=list(range(48,58))
#         v=list(range(65,91))
#         w=list(range(97,123))
#         x=u+v+w
#         y=list(random.choices(x,k=8))
#         z=list(map(chr,y))
#         z1=" ".join(z)
#         z3=z1.replace(" ","",)
#         while z3.isalpha()==True:
#             s1=random.choice(z3)
#             s2=random.choice(['0','1','2','3','4','5','6','7','8','9'])
#             z4=z3.replace(s1,s2)
#             return z4
#         return z3
# closure=Label()	
# ###############################################################################
# for arq in f1:
#     df3=pd.read_csv(arq)
#     # print()
#     # print(df3['Assunto'].value_counts())
#     for row in range(len(df3)):
#         l7=df3.loc[row,['ID do ticket','Assunto','Nome do Requisitante']].tolist()
#         a0,a1,a2=l7
#         closure.s0=a0
#         closure.s1=a1
#         closure.s2=a2
#         if a1 in l3:
#            print('ok')

                    

      