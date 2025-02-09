import pandas as pd
import fnmatch
import os
import os.path
from abc import ABC, abstractmethod
from unidecode import unidecode
import platform
import charset_normalizer
if platform.system()=='Windows':
	os.system('cls')
else:
	os.system('clear')
if platform.system()=='Windows':
	path=r"c:%HOMEPATH%\Downloads"
	u=os.path.expandvars(path)
else:
	path=r"$HOME/Downloads"
	u=os.path.expandvars(path)
v=[]
w=[]
for file in os.listdir(u):
	if fnmatch.fnmatch(file,'*.csv'):
		v.append(file)
		for m in range(len(v)):
			if platform.system()=='Windows':
				w.append(u+"\x5c"+v[m])
			w.append(u+"/"+v[m])
if len(w)>1:
	w.pop(0)
#######################################################
class Base(ABC):
	def __init__(self,*args):
		self.a0='script'
		self.a1='tabela'
	@abstractmethod
	def f0(self):
		pass

class Label(Base):
	def __init__(self,*args):
		super().__init__(*args)
		self.a2=v
		self.a3='text'
		self.a4='numeric'

	def f0(self):
		l1=[]
		for x in v:
			with open(x,'rb') as f1:
				data=f1.read()
				x1=charset_normalizer.detect(data)
				l1.append(data.decode(x1['encoding']))
				for y in l1:
					if ';' in y:
						return ';'
					else:
						return ','
label=Label()				

########################################################
if platform.system()=='Windows':
	os.chdir(u+'\x5c')
else:
	os.chdir(u+'/')
for k in range(len(v)):
	num_str=str(k)
	df=pd.read_csv(label.a2[k],sep=f'{label.f0()}')
	lc=df.columns.tolist()		
	l0=df.dtypes.tolist()
	l1=list(zip(lc,l0))
	# print(type(l1[0][0]))
	with open(f'{label.a0+num_str}.sql','w') as f:
		f.write(f'CREATE TABLE {label.a1+num_str}(')
		for n in range(len(l1)):
			if l1[n]==l1[-1]:
				if l1[n][1]=='object':
					f.write(f'"{unidecode(l1[n][0])}" {label.a3});\n')
				else:
					f.write(f'"{unidecode(l1[n][0])}" {label.a4});\n')
			else:
				if l1[n][1]=='object':
					f.write(f'"{unidecode(l1[n][0])}" {label.a3},\n')
				else:
					f.write(f'"{unidecode(l1[n][0])}" {label.a4},\n')
		f.write(f"COPY {label.a1+num_str} FROM '/docker-entrypoint-initdb.d/{label.a2[k]}' DELIMITER \'{label.f0()}\' CSV HEADER;\n")

					









	




			
			
	
