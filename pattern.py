from matplotlib import pyplot as plt
import pandas as pd

df=pd.read_csv('E:\OneDrive\Desktop\jet.csv')

x=df['Mach No.']
y1=df['1']
y2=df['2']
y3=df['3']
y4=df['4']
plt.style.use('bmh')
plt.xlabel('mach')
plt.ylabel('thrust')

plt.plot(x,y1,label='1')
plt.plot(x,y2,label='2', )
plt.title('variation in thrust')

plt.legend(loc='right')
plt.show()
