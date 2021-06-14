from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Login")
root.geometry("500x500")

root.config(bg="dark slate grey")

 #Name and Surname labels and entries
name_label = Label(root, text="Enter your name")
name_label.place(x=10,y=10)
surname_label = Label(root, text="Enter Surname")
surname_label.place(x=10,y=50)
name_entry= Entry(root)
name_entry.place(x=100,y=10)
surname_entry = Entry(root)
surname_entry.place(x=100,y=50)

email_label = Label(root, text="Enter your email: ")
email_label.place(x=10, y=100)
email_entry = Entry(root)
email_entry.place(x=100,y=100)



id_entry = Entry(root)
id_entry.config(state='readonly')
id_entry.place(x=150,y=150)



def details():
    name = name_entry.get()
    surname = surname_entry.get()
    email = str(email_entry.get())


    if "@" in email_entry.get():
        id_entry.config(state='normal')

    else:
        messagebox.showinfo(title='Alert!', message="Please enter valid email adress!")
        id_entry.config(state='readonly')
        email_entry.delete(0,END)

def id_check():
    try:
        Id = int(id_entry.get())
        id_ls = id_entry.get()

        year = id_entry.get()[1]
        year2 = id_entry.get()[0:2]

        if type(Id) == type(str()) or len(id_ls) != 13:
            raise ValueError
        elif int(year) <= 3:
            messagebox.showinfo(title="Play!", message="Lets Play!")
            import lotto
            root.destroy()
        elif int(year2) >3 and int(year2) > 21:
            messagebox.showinfo(title="Play!", message="Lets Play!")
            import lotto
            root.destroy()
        else:
            #x = int(year) -3
            messagebox.showinfo(title="Under Age", message="Your are too young to play")
    except ValueError:
        messagebox.showerror(title="Invalid Id", message="Please enter valid ID")
        id_entry.delete(0,END)

email_validator = Button(root, text="Enter Id number: ", command=details)
email_validator.place(x=10, y=150)

login_btn = Button(root, text ="login", command=id_check)
login_btn.place(x=10, y=250)
root.mainloop()

