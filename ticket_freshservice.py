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
l3=sorted(l0+l1+l2)
# lx=list(enumerate(l3))
# print(lx)
os.chdir(os.path.expandvars(r'c:%HOMEPATH%\Downloads'))
f1=glob.glob('*.csv')
###############################################################################
class Base(ABC):
    def __init__(self,*args):
        self.s0=None
        self.s1=None
        self.s2=None
        self.s03='Usuário: | '
        self.s04='Usuário: | Senha: 12345678'
    
    @abstractmethod
    def pwdgen(self):
        pass
        
class Label(Base):
    def __init__(self,*args):
        super().__init__(*args)
        self.s05='Concedido acesso a caixa compartilhada da UE para , conforme solicitado.'
        self.s06='Removido , da caixa compartilhada da UE conforme solicitado.'
        self.s07='Segue informações da lista de usuários:'
        self.s08='Conforme anexo, solicitado alteração de Licença Office365 pela Prodam.'
        self.s09='Concedido a permissão para a pasta na rede conforme solicitado.'
        self.s10='Removido a permissão para a pasta na rede conforme solicitado.'
        self.s11='#BC Configurar permissões de Caixa de E-mail compartilhada'
        self.s12='#BC Listar membros da Caixa de E-Mail Compartilhada @SME'
        self.s13='#BC Alteração de Licença - Office 365'
        self.s14='#BC Configurar permissão de pastas ou arquivos de rede'
        self.s15='#BC Remoção de acesso a Caixa de Correio Compartilhada @SME'
   
    def pwdgen(self):
        u=list(range(48,58))
        v=list(range(65,91))
        w=list(range(97,123))
        x=u+v+w
        y=list(random.choices(x,k=8))
        z=list(map(chr,y))
        z1=" ".join(z)
        z3=z1.replace(" ","",)
        while z3.isalpha()==True:
            s1=random.choice(z3)
            s2=random.choice(['0','1','2','3','4','5','6','7','8','9'])
            z4=z3.replace(s1,s2)
            return z4
        return z3
closure=Label()	
###############################################################################
l4=[[f'{closure.s05}',l3[24],f'{closure.s11}'],[f'{closure.s06}',l3[38],f'{closure.s15}'],[f'{closure.s07}',l3[32],f'{closure.s12}'],[f'{closure.s08}',l3[43],f'{closure.s13}'],[f'{closure.s09}',l3[46],f'{closure.s14}'],[f'{closure.s10}',l3[50],f'{closure.s14}']]
l5=['Reset de Senha SEI / Wi-Fi','Alteração da senha do e-mail @SME','Alterar senha no domínio Educação','Criar Usuário no Domínio Educação','Criar conta de e-mail @SME','Excluir Autenticação de Dois Fatores @SME','Criar conta de e-mail @EDU','Excluir conta de e-mail @SME',\
	'Alterar conta de e-mail @EDU - Campo nome do Usuário','Recuperar conta de e-mail @SME','Alterar Caixa de Correio Compartilhada @SME - campo "Nome"','Alterar conta de e-mail @EDU - Campo endereço de e-mail','Alterar caixa de correio compartilhada @SME - campo "Endereço de E-mail"','Conta inacessível @SME',\
    'Alterar conta de e-mail @SME - Campo "Endereço de E-mail"','Criação de usuário SEI','Não recebe/ envia e-mail @SME','Alterar conta de e-mail @SME - Campo "Nome de Usuário"','Desabilitar usuário do domínio Educação','Criar Usuário SEI','E-mail : Alteração de Senha E-mail @EDU']
l6=[[f'{closure.s03}',l3,l5]]
# print(l6)
# print()
# # # print(l4[5][1])
for arq in f1:
    df3=pd.read_csv(arq)
    # print()
    # print(df3['Assunto'].value_counts())
    for row in range(len(df3)):
        l7=df3.loc[row,['ID do ticket','Assunto','Nome do Requisitante']].tolist()
        a0,a1,a2=l7
        closure.s0=a0
        closure.s1=a1
        closure.s2=a2
        if a1 in l3:
            for m,n,o in l4:
                if a1==n:
                    print('######################################################################################')
                    print(f'\nPrezado(a) {closure.s2},conforme atendimento ao seu chamado de número SR-{closure.s0}:\n\nDescrição: {closure.s1}\n\nSolução: {m}\n\nConclusão: Chamado finalizado após aplicada a solução acima.')
                    print(f'\n{o}')
                    print(f'\n######################################################################################')
                    

      