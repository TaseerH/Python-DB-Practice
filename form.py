import mysql.connector
import numpy as np
from tkinter import *
import urllib.request
import re
from tkinter.tix import *

root = Tk()
root.title("Entry Form")
frame = Frame(width="1920",height="1000")
frame.pack()
swin = ScrolledWindow(frame, width=1920, height=900)
swin.pack()
root = swin.window

mydb = mysql.connector.connect(host= 'localhost', 
                               user= 'root', 
                               port= '3307',
                               password= None, 
                               database='movies1')
mycursor = mydb.cursor()

query = "insert into practice (first_name, second_name, age, school) values (%s,%s,%s,%s)"
query2 = "select * from practice;"

warn = Label(root, text=".")
warn.grid(row=0, column = 3)

def show_data():
    mycursor.execute(query2)
    i=7 
    j = 0
    for first_name in mycursor: 
        for j in range(len(first_name)):
            e = Entry(root, width=35, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, first_name[j])
        i=i+1

def submit():
    
    
    if (f_name.get()).isalpha() == TRUE and (l_name.get()).isalpha() == TRUE:
    
        if re.match("^[0-9 -]+$", age.get()):
            
            warn['text'] = ""
            
            mydata = (f_name.get(), l_name.get(), age.get(), school.get())
            mycursor.execute(query, mydata)
            mydb.commit()
            
            f_name.delete(0, END)
            f_name.insert(0, "")
            l_name.delete(0, END)
            l_name.insert(0, "")
            age.delete(0, END)
            age.insert(0, "")
            school.delete(0, END)
            school.insert(0, "")

            data_entry = Label(root, text = "Data has been entered!")
            data_entry.grid(row=4, column = 2)
            
            show_data()

        
        else:
            warn['text'] = ""
            warn.config(text = "Age should be a number!")
               
    else:
        warn['text'] = ""
        warn.config(text = "Name cannot have a number in it!")

f_name_label = Label(root, text = "First Name:")
f_name_label.grid(row=0, column = 0)

f_name = Entry(root, width = 30)
f_name.grid(row=0, column=1, padx=20)

l_name_label = Label(root, text = "Last Name:")
l_name_label.grid(row=1, column = 0)

l_name = Entry(root, width = 30)
l_name.grid(row=1, column=1, padx=20)

age_label = Label(root, text = "Age:")
age_label.grid(row=2, column = 0)

age = Entry(root, width = 30)
age.grid(row=2, column=1, padx=20)

school_label = Label(root, text = "School:")
school_label.grid(row=3, column = 0)

school = Entry(root, width = 30)
school.grid(row=3, column=1, padx=20)

submit_btn = Button(root, text="Add records to Database", command=lambda: submit())
submit_btn.grid(row=4, column = 0, columnspan= 2, pady=10, padx= 10, ipadx=100)

submit_btn = Button(root, text="Show Database", command=lambda: show_data())
submit_btn.grid(row=5, column = 0, columnspan= 2, pady=10, padx= 10, ipadx=100)

root.mainloop()