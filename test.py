from sqlalchemy import create_engine
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#db_connection_str = 'mysql+pymysql://root:@localhost:3307/movies1'


mydb = mysql.connector.connect(host= 'localhost', 
                               user= 'root', 
                               port= '3307',
                               password= None, 
                               database='movies1')

mycursor = mydb.cursor()

mycursor.execute("select title, budget, revenue from movie limit 25")
result = mycursor.fetchall

title = []
budget = []
revenue = []

for i in mycursor:
    title.append(i[0])
    budget.append(i[1]/1000000)
    revenue.append(i[2]/1000000)


print ("Titles:", title)
print("Budget:", budget)
print("Revenue", revenue)

plt.figure(figsize=(100, 100))
plt.scatter(title, budget)
plt.scatter(title, revenue)
plt.plot(title, budget)
plt.plot(title, revenue)
plt.ylim(0, 1100)
plt.xlim(0, 25)
plt.xlabel("Titles")
plt.ylabel("Budgets per 1000000/ Revenue per 1000000")
plt.xticks(rotation = 85)
plt.show()
mydb.close()
