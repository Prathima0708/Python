# number=int(input("Enter a Number: "))

# if number %2==0:
#     if number >=1 and number<=50:
#         print("Its a Even Weird Number")
#     elif number >50 and number<=75:
#         print("Its a Even Big Number")
#     else:
#         print("Its a Even Numner")
# elif number %2 !=0:
#     if number>=1 and number<=50:
#         print("Its a Odd Weird Number")
#     elif number>50 and number<=75:
#         print("Its a Odd Big Number")
#     else:
#         print("Its a Odd Number")

# from sqlite3 import connect
# import mysql.connector
# import pandas as pd

# mydb = mysql.connector.connect(host="169.63.187.196",user="cetasuser",passwd="Cetas21$!uat",database="airdb")

# mycursor =mydb.cursor()

# mycursor.execute("select * from datasource")

# # # result=mycursor.fetchall()

# for i in mycursor:
#     print(i)

# for i in result:
#     print(i)
















# import json
# import csv
# with open('app.json')as file:
#     data=json.load(file)

# with open('users.csv','w')as file:
#     csv_file=csv.writer(file)
#     csv_file.writerow(["Name","Age","Marks","Country"])
#     for item in data["result"]:
#         csv_file.writerow([item['name'],item['age'],item['marks'],item['country']])


from calendar import MONDAY
from xml.dom import DOMException
from xml.dom.expatbuilder import DOCUMENT_NODE
from requests.api import head
import requests
import csv

url='http://api.coincap.io/v2/assets'

headers={
    'Accept':'application/json',
    'Content-Type':'application/json'

}
response=requests.request("GET",url,headers=headers,data={})
myjson=response.json()
# print(myjson)

ourdata=[]
csvheader=['SYMBOL','NAME','PRICEUSD','ID','SUPPLY','EXPLORER']
for x in myjson['data']:
     
    listing=[x['symbol'],x['name'],x['priceUsd'],x['id'],x['supply'],x['explorer']]
    ourdata.append(listing)
# print(ourdata)


with open('users.csv','w',encoding='UTF8',newline='')as f:
    writer=csv.writer(f)
    writer.writerow(csvheader)
    writer.writerows(ourdata)

print("done")

