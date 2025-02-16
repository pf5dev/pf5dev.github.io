import os
import os.path
import glob
import pandas as pd
import random
os.system('cls')
os.chdir(r'C:\Users\eu\Documents\sut')
df0=pd.read_excel('Planilha de Categorias (Freshservice).xlsx',sheet_name='Acessos')
l0=df0['Título do Chamado'].tolist()
df1=pd.read_excel('Planilha de Categorias (Freshservice).xlsx',sheet_name='E-mail')
l1=df1['Título do Chamado'].tolist()
df2=pd.read_excel('Planilha de Categorias (Freshservice).xlsx',sheet_name='Pastas')
l2=df2['Título do Chamado'].tolist()
l3=sorted(l0+l1+l2)
lx=list(enumerate(l3))
print(lx)
path=r"c:%HOMEPATH%\Downloads"
u=os.path.expandvars(path)
os.chdir(u)
s0=glob.glob('*.csv')
# ##############################################################################
# class Label:
#     def __init__(self,*args):
#         self.s0='Usuário: | '
#         self.s1='Usuário: | Senha: 12345678'
#         self.s2='Concedido acesso a caixa compartilhada da UE para , conforme solicitado.'
#         self.s3='Removido , da caixa compartilhada da UE conforme solicitado.'
#         self.s4='Segue informações da lista de usuários:'
#         self.s5='Conforme anexo, solicitado alteração de Licença Office365 pela Prodam.'
#         self.s6='Concedido a permissão para a pasta na rede conforme solicitado.'
#         self.s7='Removido a permissão para a pasta na rede conforme solicitado.'
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
# ##############################################################################
for arq in s0:
    df3=pd.read_csv(arq)
    # print()
    print(df3['Assunto'].value_counts())
    for row in range(len(df3)):
        l4=df3.loc[row,['ID do ticket','Assunto','Nome do Requisitante']].tolist()
        a0,a1,a2=l4
        if a1 in l3:
            match l3.index(a1):
                case 24|26|31|32|38|43|46|50:
                    print(a1)
                

      