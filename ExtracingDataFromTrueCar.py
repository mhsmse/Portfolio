import requests
from bs4 import BeautifulSoup
import lxml.html as lxl
import re
import mysql.connector

cnx=mysql.connector.connect(user='root',host='localhost',password='',
database="carfinal",charset='utf8')


cursor=cnx.cursor()
cursor.execute('DELETE FROM carinfo')

MAX_PAGE = 333
def urls_scraping(base_url = 'https://www.truecar.com/used-cars-for-sale/listings/'):
    pages = []
    for i in range(1, MAX_PAGE+1):
        pages.append(base_url + '?page=' + str(i))
    return pages
final_list=[]
model=str(input())
for page in urls_scraping():
    r=requests.get(page)
    soup=BeautifulSoup(r.text,'html.parser')
    val=soup.findAll('div',attrs={'class':"linkable card card-shadow vehicle-card _1qd1muk"})
    for i in val:
        link=i.find('a',{'class':"linkable order-2 vehicle-card-overlay"}).attrs['href']
        if re.search(model,link):
            base='https://www.truecar.com'
            slcak=base+link
            s=requests.get(slcak)
            slacksoup=BeautifulSoup(s.text,'html.parser')
            mileage=slacksoup.find('p',{'class':"margin-top-1"})
            modelcar=slacksoup.find('div',{'class':"heading-2"})
            price=slacksoup.find('div',{'class':'heading-2 margin-top-3'})
            x=str(modelcar.text)
            y=mileage.text.replace(',','')
            z=price.text.replace(',','')
            z1=z.replace('$','')
            y1=float(y)
            z2=float(z1)
            print(z2)
            print(type(z2))

            cursor.execute('INSERT INTO carsinfo VALUES(\'%s\',\'%f\',\'%f\')' %(x,y1,z2))
            cnx.commit()
                
cnx.close()                               
            