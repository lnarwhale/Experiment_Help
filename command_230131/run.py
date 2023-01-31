import pandas as pd
import numpy as np


fi=open('data_cvm.csv',"r")
for line in fi:
	print(line)
fi.close()

na=input("input the name: ")
vo=float(input("input the volume(ml): "))
c=float(input("input the concentration(mol/L): "))

df=pd.read_csv('0data.csv')
t=df[df.name==na].index
loc=t[0]
M=df.iloc[loc,1]
m=M*c*vo/1000
print("---------------")
print("你需要称取（g）")
print(m)
print("-----appendix------")
print("其相对分子量大小为")
print(M)
