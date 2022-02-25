# from sqlite3 import Cursor, connect
# import mysql.connector
# import pandas as pd

# mydb = mysql.connector.connect(host="169.63.187.196",user="cetasuser",passwd="Cetas21$!uat",database="airdb")
# sql_query=pd.read_sql_query("select *from datasource",mydb)
# sql_query.to_csv(r'E:\tmp1.csv',index=False)

# mycursor =mydb.cursor()

# mycursor.execute("select * from datasource")

# # result=mycursor.fetchall()

# for i in mycursor:
#     print(i)

# for i in result:
#     print(i)



# query="select data_source_name ,data_source_type from datasource"
# mycursor.execute(query)

# myalldata=mycursor.fetchall()

# all_data_sname=[]
# all_data_stype=[]

# for data_source_name ,data_source_type in myalldata:
#     all_data_sname.append(data_source_name)
#     all_data_stype.append(data_source_type)

# dic={'data_source_name':all_data_sname,'data_source_type':all_data_stype}
# df=pd.DataFrame(dic)
# df_csv=df.to_csv('E:/softcopy.csv')

















#python examples-
# print("welcome to quiz")
# playing=input("do you wnat to play? ")
# if playing.lower() !="yes":
#     quit()
# print("lets play!")
# score=0

# answer=input("what does RAM stand for ? ")
# if answer.lower()=="random access memory":
#     print("Correct")
#     score+=1
# else:
#     print("Incorrect")

# answer=input("what does ROM stand for ? ")
# if answer.lower()=="read only memory":
#     print("Correct")
#     score+=1
# else:
#     print("Incorrect")

# answer=input("what does GPU stand for ? ")
# if answer.lower()=="graphics processing unit":
#     print("Correct")
#     score+=1
# else:
#     print("Incorrect")

# answer=input("what does CPU stand for ? ")
# if answer.lower()=="central processing unit":
#     print("Correct")
#     score+=1
# else:
#     print("Incorrect")

# answer=input("what does PSU stand for ? ")
# if answer.lower()=="power supply":
#     print("Correct")
#     score+=1
# else:
#     print("Incorrect")

# print("your score is : " + str(score))


#calculator program :
# def add(a,b):
#     result=a+b
#     print(result)

# def sub(a,b):
#     result=a-b
#     print(result)

# def mul(a,b):
#     result=a*b
#     print(result)

# def div(a,b):
#     result=a/b
#     print(result)

# a=int(input("enter the first number : "))
# b=int(input("enter the second number : "))
# op=input("enter the operator ")

# if op=="+":
#     add(a,b)
# elif op=="-":
#     sub(a,b)
# elif op=="*":
#     mul(a,b)
# elif op=="/":
#     div(a,b)
# else:
#     print("invalid operator")

import tkinter as tk
from unittest import result
calculation=""

def add_to_calculation(symbol):
    global calculation
    calculation+=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_filed()
        text_result.insert(1.0,"error")

def clear_filed():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")

root=tk.Tk()
root.geometry("300x275")

text_result=tk.Text(root,height=2,width=16,font=("Arial",24))
text_result.grid(columnspan=5)

btn_1=tk.Button(root,text="1",command=lambda:add_to_calculation(1),width=5,font=("Arial",14))
btn_1.grid(row=2,column=1)

btn_2=tk.Button(root,text="2",command=lambda:add_to_calculation(2),width=5,font=("Arial",14))
btn_2.grid(row=2,column=2)

btn_3=tk.Button(root,text="3",command=lambda:add_to_calculation(3),width=5,font=("Arial",14))
btn_3.grid(row=2,column=3)

btn_4=tk.Button(root,text="4",command=lambda:add_to_calculation(4),width=5,font=("Arial",14))
btn_4.grid(row=3,column=1)

btn_5=tk.Button(root,text="5",command=lambda:add_to_calculation(5),width=5,font=("Arial",14))
btn_5.grid(row=3,column=2)

btn_6=tk.Button(root,text="6",command=lambda:add_to_calculation(6),width=5,font=("Arial",14))
btn_6.grid(row=3,column=3)

btn_7=tk.Button(root,text="7",command=lambda:add_to_calculation(7),width=5,font=("Arial",14))
btn_7.grid(row=4,column=1)

btn_8=tk.Button(root,text="8",command=lambda:add_to_calculation(8),width=5,font=("Arial",14))
btn_8.grid(row=4,column=2)

btn_9=tk.Button(root,text="9",command=lambda:add_to_calculation(9),width=5,font=("Arial",14))
btn_9.grid(row=4,column=3)

btn_0=tk.Button(root,text="0",command=lambda:add_to_calculation(0),width=5,font=("Arial",14))
btn_0.grid(row=5,column=2)

btn_plus=tk.Button(root,text="+",command=lambda:add_to_calculation("+"),width=5,font=("Arial",14))
btn_plus.grid(row=2,column=4)

btn_minus=tk.Button(root,text="-",command=lambda:add_to_calculation("-"),width=5,font=("Arial",14))
btn_minus.grid(row=3,column=4)

btn_mul=tk.Button(root,text="*",command=lambda:add_to_calculation("*"),width=5,font=("Arial",14))
btn_mul.grid(row=4,column=4)

btn_div=tk.Button(root,text="/",command=lambda:add_to_calculation("/"),width=5,font=("Arial",14))
btn_div.grid(row=5,column=4)

btn_open=tk.Button(root,text="(",command=lambda:add_to_calculation("("),width=5,font=("Arial",14))
btn_open.grid(row=5,column=1)

btn_close=tk.Button(root,text=")",command=lambda:add_to_calculation(")"),width=5,font=("Arial",14))
btn_close.grid(row=5,column=3)

btn_equals=tk.Button(root,text="=",command=evaluate_calculation,width=11,font=("Arial",14))
btn_equals.grid(row=6,column=3,columnspan=2)

btn_clear=tk.Button(root,text="C",command=clear_filed,width=11,font=("Arial",14))
btn_clear.grid(row=6,column=1,columnspan=2)



root.mainloop()


#guessing game -
# import random
# top_of_range=input("type a number : ")

# if top_of_range.isdigit():
#     top_of_range=int(top_of_range)

#     if top_of_range==0:
#         print("please type a number larger than 0 next time")
#         quit()
# else:
#     print("please type a number next time")
#     quit()

# random_number=random.randint(0,top_of_range)
# guesses=0

# while True:
#     guesses+=1
#     user_guess=input("make a guess : ")
#     if user_guess.isdigit():
#         user_guess=int(user_guess)
#     else:
#         print("please type a number next time")
#         continue
#     if user_guess==random_number:
#         print("you got it !")
#         break
#     elif user_guess>random_number:
#         print("your guess is above the number ,guess lower !")
#     else:
#         print("your guess is below the number ,guess higher !")

# print("you got it in " + str(guesses) + " guesses")

#python exmaples:
# thislist = ["apple", "banana", "cherry"]
# print(type(thislist))

# if "appdle" in thislist:
#     print("yes,apple is present in the list")
# else:
#     print("apple is not present")

# thislist.append("grapes")
# print(thislist)

# thislist.insert(1,"orange")
# print(thislist)

# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# for x in range(len(thislist)):
#     print(thislist[x])

# thislist.pop()
# print(thislist)

# thislist.remove("banana")
# print(thislist)