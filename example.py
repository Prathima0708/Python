# from pandas import DataFrame
# import json
# import pandas as pd
# import numpy as np
# d={
#     'Name':['John','abc','xyz'],
#     'Age':[23,34,33],
#     'score':[87,99,99]

# }
# df=pd.DataFrame(d,index=['A','B','C'])
# # # # # df=pd.read_csv("E:/softcopy.csv")
# print(df)
# print(df*2)
# # print(df['score'].max())

# # l=df['Name'][df['score']==99]
# # print(l)

# # rows,col=df.shape
# # print(rows)

# # print(df.head(2))



# d1={
#     'Name':['efg','abc','xyz'],
#     'Age':[43,54,73],
#     'score':[97,19,99]

# }
# df1=pd.DataFrame(d1,index=['A','B','C'])
# # # print(df[['Age','score']]* df1[['Age','score']])

# print(df1)
# # print(df+df1)

# print(df1['Name']=='efg')

# raw_data="""{
#     "city":["india","rome","japan"],
#     "rank":["1st","2nd","3rd"],
#     "score":[33,44,55]
#     }"""
# data=json.loads(raw_data)
# print(data)

# df=DataFrame(data)
# print(df)

# df=pd.DataFrame({'c1':[34,45,34],'c2':['a','b','c'],'c3':[1,2,3]})
# print(df)
# print(df.columns)
# print(df.index)
# print(df['c3'].sum())

# def power(x):
#     return x ** 3
# r=df['c3'].apply(power)   
# print(r)

# print(df['c1'].value_counts())
# print(df['c1'].unique())

# print(df['c1'].nunique())  #to know how many unique values

# s=df.sort_values(by='c1')  #sorting
# print(s)

# df=pd.DataFrame({'c1':[34,45,34,49],'c2':['a','b','c',np.nan],'c3':[1,np.nan,2,3]})
# print(df)

# print(df.isnull())
# print(df.dropna())
# print(df.fillna('hi'))

# import copy
# l1 = [120, 210, [11,33], 240] # using deepcopy for copying l1
# l3 = copy.deepcopy(l1)
# print ("The original elements in the list l1")
# for i in range(0,len(l1)):
#  print (l1[i],end=" ")
#  print("\r")
# # Altering the Deepcopy list l3
# l3[1] = 70
# # Change made at 2nd position is seen in list l2
# print ("The new list of elements after deep copying ")
# for i in range(0,len( l1)):
#  print (l3[i],end=" ")
#  print("\r")
# ### The Actual List l1 remains unchanged
# print ("The original elements after deep copying")
# for i in range(0,len( l1)):
#  print (l1[i],end=" ")

# df=pd.read_csv("E:/softcopy.csv")
# print(df)
# print(df.tail(7))
# print(df['data_source_type'])

# importing pandas module
# import pandas as pd 
 
# # Define a dictionary containing employee data 
# data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
#         'Age':[27, 24, 22, 32], 
#         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
   
# # Define a dictionary containing employee data 
# data2 = {'Name':['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'], 
#         'Age':[17, 14, 12, 52], 
#         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
#         'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
# # Convert the dictionary into DataFrame  
# df = pd.DataFrame(data1,index=[0, 1, 2, 3])
 
# # Convert the dictionary into DataFrame  
# df1 = pd.DataFrame(data2, index=[4, 5, 6, 7])
 
# # print(df)
# # print(df1)

# # using a .concat() method
# frames = [df, df1]
 
# res1 = pd.concat(frames)



# print(res1)


#json to dataframe:

# mydic={
#     'name':['alex','ravi','ron'],
#     'id':[1,2,3],
#     'maths':[50,35,66],
#     'english':[55,88,90]
# }

# df=pd.DataFrame(data=mydic)
# df_j=df.to_json(orient='split')
# print(df_j)
# df=pd.read_json(df_j,orient='split')
# print(df)

#CSV to dataframe:

# df=pd.read_csv('users.csv')
# print(df)


#dataframe to csv:
# mydic={
#     'name':['alex','ravi','ron'],
#     'id':[1,2,3],
#     'maths':[50,35,66],
#     'english':[55,88,90]
# }
# df=pd.DataFrame(data=mydic)
# # df_j=df.to_json(orient='split')
# # print(df_j)
# # df=pd.read_json(df_j,orient='split')
# # print(df)
# df.to_csv('new.csv',index=False)

# def translate(phrase):
#     translation=""
#     for letter in phrase:
#         if letter in "AEIOUaeiou":
#             translation=translation + "g"
#         else:
#             translation=translation + letter
#     return translation
# print(translate(input("enter a phrase: ")))

# for number in range(1,10):
#     if number % 2==0:
#         print(number)


# s=input("enter a string : ")

# rev=(s[::-1])

# if rev==s:
#     print("yes")
# else:
#     print("no")



# import string


# string=input("enter a string : ")
# n=len(string)
# flag=0
# if n%2:
#         mid=n//2+1
# else:
#         mid= n//2
# start=0
# end= mid
# while(start <mid and end<n):
#         if(string[start]== string[end]):
#             start= start+1
#             end= end+1
#         else:
#             flag=1
#             break
# if flag==0:
#         print("symmetrical")
# else:
#         print("not symmetrical")



string = input("enter a string : ")
half = int(len(string) / 2)

if len(string) % 2 == 0: # even
	first_str = string[:half]
	second_str = string[half:]
    
else: # odd
	first_str = string[:half]
	second_str = string[half+1:]
print(first_str)
print(second_str)
# symmetric
if first_str == second_str:
	print(string, 'string is symmertical')
else:
	print(string, 'string is not symmertical')

rev=(string[::-1])
# palindrome
if string==rev:
# if first_str == second_str[::-1]: 
	print(string, 'string is palindrome')
else:
	print(string, 'string is not palindrome')
