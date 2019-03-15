import sqlite3
con=sqlite3.connect('mydb.sqlite3')
#import other_db_name
#con=otherdb.comconnect(user='',password='',host='',database='')
cur=con.cursor()
q='''CREATE TABLE IF NOT EXISTS LOGDATA(
    IP VARCHAR(100), DATE VARCHAR(100), PICS VARCHAR(100), WEBSITE VARCHAR(100))'''
cur.execute(q)

import urllib.request as u
url='https://www.jafsoft.com/searchengines/log_sample.html'
f=u.urlopen(url)
import re #Reguler expression module
for line in f:
    #print(type(line))
    line=line.decode()
    #print(type(line))
    m=re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{1,3}).*?(\d{1,2}/[a-zA-Z]{3}/\d{1,4}).*GET\s+/(pics/(\w+\.\w+))?.*http[s]?://([a-zA-Z0-9.]+).*',line)
    if m!=None:
        ip=m.group(1)
        date=m.group(2)
        pics=m.group(4)
        wb=m.group(5)
        if pics == None:
            pics='No Image'

        #print(ip,date,pics,wb)
        #q=f"INSERT INTO LOGDATA VALUES('{ip}','{date}','{pics}','{wb}')"
        #cur.execute(q)
#con.commit()
q='SELECT * FROM LOGDATA'
cur.execute(q)
result=cur.fetchall()
#print(result)

#exporting data in CSV
import csv
f=open('dbdump.csv','w',newline='')
wt=csv.writer(f)
h=['IP','DATE','PICS','WEBSITE']
wt.writerow(h)
for row in result:
    wt.writerow(row)
f.close()

#using Pandas to dump the file
import pandas as pd
l=[[10,20,30],[40,50,60]]
df1=pd.DataFrame([[10,20,30],[40,50,60]])
#print(df1)
df2=pd.DataFrame(result)
df2.to_csv('out5.csv',header=None,index=None)
df2.to_excel('out6.xlsx',header=None,index=None)
df2.to_json('t1.json')
print(df2)

L=[('a','b'),('c','d')]
df2=pd.DataFrame(L)
print(df2)
df2.to_json('t.json')
