from itertools import count
from multiprocessing import connection
from unittest import result
from sklearn import tree
import mysql.connector
import re



cnx=mysql.connector.connect(user='root',host='localhost',password='',
database="carfinal",charset='utf8')
queryselect= "select mileage from carsinfo"
cursor=cnx.cursor()
cursor.execute(queryselect)
rowmilage= [item[0] for item in cursor.fetchall()]
queryselect1="select price from carsinfo"
cursor.execute(queryselect1)
rowprice= [item[0] for item in cursor.fetchall()]
queryselect2="select model from carsinfo"
cursor.execute(queryselect2)
rowmodel1=[item[0] for item in cursor.fetchall()]
rowmodel=[]
for item in rowmodel1:
    result=re.search(r'(^[0-9]+).',item)
    extra=result.group(1)
    rowmodel.append(extra)

count1=len(rowmodel)
part=0
reflist=[]
for i in range (count1):
    slack=[]
    slack.append(rowmodel[part])
    slack.append((rowmilage[part]))
    reflist.append(slack)
    part=part+1

clf=tree.DecisionTreeClassifier()
clf=clf.fit(reflist,rowprice)
data=[]
data2=[]
new_data=input('enter car model:')
data.append(new_data)
new_data=float(input('enter car mileage:'))
data.append(new_data)
data2.append(data)
answer=clf.predict(data2)
print('the predicted price is:')
print(answer)










cnx.close()
cursor.close()


