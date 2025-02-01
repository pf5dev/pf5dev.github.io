import random
import os
import pandas as pd
x=True
while x:
	os.system('cls')
	l0=['Reset de Senha SEI / Wi-Fi','Alteração da senha do e-mail @SME','Configurar permissões de Caixa de E-mail compartilhada','Alterar senha no domínio Educação',\
		'Listar membros da Caixa de E-Mail Compartilhada @SME','Alteração de Licença - Office 365','Criar Usuário no Domínio Educação','Criar conta de e-mail @SME','Excluir Autenticação de Dois Fatores @SME',\
			'Criar conta de e-mail @EDU','Configurar permissão de pastas ou arquivos de rede','Excluir conta de e-mail @SME','Remoção de acesso a Caixa de Correio Compartilhada @SME','Alterar senha domínio Rede',\
				'Alterar conta de e-mail @EDU - Campo nome do Usuário','Recuperar conta de e-mail @SME','Alterar Caixa de Correio Compartilhada @SME - campo "Nome"',\
					'Alterar conta de e-mail @EDU - Campo endereço de e-mail','Alterar caixa de correio compartilhada @SME - campo "Endereço de E-mail"','Conta inacessível @SME','Alterar conta de e-mail @SME - Campo "Endereço de E-mail"',\
						'Criação da Caixa de Correio Compartilhada','Criação de usuário SEI','Não recebe/ envia e-mail @SME','Alterar conta de e-mail @SME - Campo "Nome de Usuário"',\
							'Desabilitar usuário do domínio Educação','Criar Usuário SEI']
	p3=input('Editar assunto [s]im / [n]ao: ')
	if p3=='s':
		os.chdir(r'C:\Users\268903258\Documents\docs_N3')
		l1=['Acessos','E-mail','Equipamentos','Impressora','Infraestrutura','Pastas','Programas e Sistemas','Rede e Internet','Servidores','Suporte Pedagógico']
		l2=list(enumerate(l1))
		print(l2)
		p0=int(input('Nome planilha: '))
		print()
		df=pd.read_excel('Planilha de Categorias (Freshservice).xlsx',sheet_name=f'{l2[p0][1]}')
		l3=list(enumerate(sorted(df['Título do Chamado'])))
		print(l3)
	print()
	l5=list(enumerate(l0))
	print(sorted(l5))
	p2=int(input('#BC: '))
	print(f'#BC {l5[p2][1]}')
	##############################################################################
	class Label:
		def __init__(self,*args):
			self.s0='Usuário: | '
			self.s1='Concedido acesso a caixa compartilhada da UE para , conforme solicitado.'
			self.s2='Removido , da caixa compartilhada da UE conforme solicitado.'
			self.s3='Segue informações da lista de usuários:'
			self.s4='Conforme anexo, solicitado alteração de Licença Office365 pela Prodam.'
			self.s5='Concedido permissão da pasta na rede conforme solicitado.'
			self.s6='Removido permissão da pasta na rede conforme solicitado.'
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
	##############################################################################
	print()
	l4=list(enumerate([f'{closure.s0}',f'{closure.s1}',f'{closure.s2}',f'{closure.s3}',f'{closure.s4}',f'{closure.s5}',f'{closure.s6}']))
	print(l4)
	print()
	p1=input('Atributo: ')
	match p1:
		case '0':
			print(f'{closure.s0}Senha: {closure.pwdgen()}')
			print()
		case '1':
			print(f'{closure.s1}')
			print()
		case '2':
			print(f'{closure.s2}')
			print()	
		case '3':
			print(f'{closure.s3}')
			print()
		case '4':
			print(f'{closure.s4}')
			print()
		case '5':
			print(f'{closure.s5}')
			print()
		case '6':
			print(f'{closure.s6}')
			print()
	p4=input('Continuar [s]im / [n]ao: ')
	if p4=='s':
		continue
	else:
		x=False