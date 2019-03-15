import pandas as pd
df=pd.read_csv('dbdump.csv',delimiter=';')
#print(df)
#df2=df['IP']
#print(df2)
#df3=df['NUMBER'].describe()
#df3=df['NUMBER'].mean()
#df3=df['NUMBER'].count()
df3=df['PICS'].value_counts()
#print(df3)

#matplot use in pandas
import matplotlib.pyplot as plt
df3.plot()
#plt.show()
df3.plot.bar()
plt.savefig('graph.png')

#put the data into excel files

writer=pd.ExcelWriter('Report.xlsx',engine='xlsxwriter')
df3.to_excel(writer,sheet_name='Data')
wb=writer.book
ws=wb.add_worksheet('graph')
ws.insert_image('B1','graph.png')
writer.close()

df4=df[df['NUMBER'] > 10]
#print(df4)
df5=df[df['PICS'].str.endswith('jpg')] #string strat,end example
#print(df5)
df6=df.groupby(['PICS']).count() #group by example
#print(df6)
df7=df.iloc[1] #Index example
#print(df7)
df8=df.iloc[1:7]
#print(df8)
df9=df.iloc[1:3,1]
#print(df9)
df10=df.iloc[1:3,1:3]
#print(df10)
df11=df.iloc[1,2]
#print(df11)
df12=df.iloc[[1,3],[2,4]]
#print(df12)
