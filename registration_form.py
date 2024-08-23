from tkinter import * 
import mysql.connector
import os
from dotenv import load_dotenv

root = Tk()
root.geometry("500x300")
root.title("Registration Form")

myLabel = Label(root, text="Registration Form", font=("Arial Bold", 18))
myLabel.grid(row=0, column=1, columnspan=3, padx=15, pady=10)

# loading the env file
load_dotenv('cred.env')

def submit_to_db():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    cursor = conn.cursor()

    # Inserting data into database
    cursor.execute("INSERT INTO registrations (name, surname, gender, contact, email) VALUES (%s, %s, %s, %s, %s)",
                   (name_value.get(), surname_value.get(), gender_value.get(), contact_value.get(), email_value.get()))

    conn.commit()

    # Close the connection
    cursor.close()
    conn.close()

    # update the user that the form is submitted
    submitted = Label(root, text="Form Submitted", fg="green")
    submitted.grid(row=6, column=2)

def click():
    submit_to_db()

def clear():
    name_value.set("")
    surname_value.set("")
    gender_value.set("")
    contact_value.set("")
    email_value.set("")


# Adding Labels
name = Label(root, text="Name:", font=("Arial",12))
surname = Label(root, text="Surname:", font=("Arial",12))
gender = Label(root, text="Gender:", font=("Arial",12))
contact = Label(root, text="Contact:", font=("Arial",12))
email = Label(root, text="Email:", font=("Arial",12))

# Adding button
button1 = Button(root, text="Submit", font=("Arial",12), command=click)
clear_button = Button(root, text="Clear", font=("Arial",12), command=clear)
close_prog = Button(root, text="Close", command=root.quit, font=("Arial",12))

# Placing the button
button1.grid(row=5, column=2, padx=15, pady=10)
clear_button.grid(row=5, column=1, padx=15, pady=10)
close_prog.grid(row=6, column=1)

# Placing them inside root
name.grid(row=1, column=0, padx=10, pady=5)
surname.grid(row=1, column=2, padx=10, pady=5)
gender.grid(row=2, column=0, padx=10, pady=5)
contact.grid(row=3, column=0, padx=10, pady=5)
email.grid(row=4, column=0, padx=10, pady=5)

# Creating Variable
name_value = StringVar()
surname_value = StringVar()
gender_value = StringVar()
contact_value = StringVar()
email_value = StringVar()

# Creating Entry
name_entry = Entry(root, textvariable=name_value)
surname_entry = Entry(root, textvariable=surname_value)
gender_entry = Entry(root, textvariable=gender_value)
contact_entry = Entry(root, textvariable=contact_value)
email_entry = Entry(root, textvariable=email_value)

# Placing the entry field for the user
name_entry.grid(row=1, column=1, padx=10, pady=5)
surname_entry.grid(row=1, column=3, padx=10, pady=5)
gender_entry.grid(row=2, column=1, padx=10, pady=5)
contact_entry.grid(row=3, column=1, padx=10, pady=5)
email_entry.grid(row=4, column=1, padx=10, pady=5) 

root.mainloop()
