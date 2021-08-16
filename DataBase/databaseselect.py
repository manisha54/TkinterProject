from tkinter import *
import sqlite3

root = Tk()
root.title('Hospital Management System')


#Database
#create a database or connect to one

conn = sqlite3.connect('Management_system.db')
#crusor class is an instance using which you can invoke methods tha execute SQlite statements
# fetch data from the resut set of queries

c = conn.cursor()

'''
#Create table
c.execute(""" CREATE TABLE addresses(
          first_name text,
          last_name text,
          address text,
          city text,
          state text,
          zipcode integer
) """)

'''
#print("Table created successfully")


def submit():
    #create a database or connect to one
    conn = sqlite3.connect('Management_system.db')
    #create cursor
    c = conn.cursor()
    #insert in to table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zip_code)",{
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zip_code':zip_code.get()
    })
    print('Address inserted successfully')
    conn.commit()
    conn.close()
    # clear the text box
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zip_code.delete(0,END)

def query():
    #create a data base or connect to one
    conn = sqlite3.connect('Management_system.db')

    #create cursor
    c = conn.cursor()

    #query of the database
    c.execute("Select *, oid FROM addresses")
    records = c.fetchall()
   # print(records)
   #loop through the results
    print_record=''
    for record in records:
       print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[6]) + "\n"

    query_label = Label(root, text=print_record)
    query_label.grid(row=8, column=0, columnspan=2)



f_name = Entry(root, width=30, bg='blue')
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30, bg='yellow')
l_name.grid(row=1, column=1)

address = Entry(root, width=30, bg='red')
address.grid(row=2, column=1)

city = Entry(root, width=30,bg='orange')
city.grid(row=3, column=1)

state = Entry(root, width=30, bg='purple')
state.grid(row=4, column=1)

zip_code = Entry(root, width=30, bg='green')
zip_code.grid(row=5, column=1)

#create a textbox lable

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)


l_name_label = Label(root, text=" LastName")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Adress")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zip_code_label = Label(root, text="Zip Code")
zip_code_label.grid(row=5, column=0)



submit_button = Button(root, text=" Add record", bg='purple', fg='red',  command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10,ipadx=100)

showrecord_button = Button(root, text="show records", bg='purple', fg='red', command=query)
showrecord_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10,ipadx=100)
#commit change
conn.commit()

conn.close()

root.mainloop()