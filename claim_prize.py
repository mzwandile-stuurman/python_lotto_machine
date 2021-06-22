import requests
from tkinter import *
from tkinter import  ttk
from tkinter import messagebox


root = Tk()
root.geometry("600x600")
root.title("Claim your prize money here!")
root.config(bg = 'dark slate grey')


class Prize_claim():
    from tkinter import ttk
    def __init__(self,master):
        self.bank_label = Label(master, text= "Bank: ")
        self.bank_label.place(x=20,y=40)

        self.banks_list = ttk.Combobox(master, text="Choose a bank.") # combobox for bank choices
        self.banks_list['values'] = ('ABSA','FNB','CAPITEC','STANDARD BANK')
        self.banks_list.current()
        self.banks_list.place(x=100,y=40)

        self.winner_name_label=Label(master, text="Name:")
        self.winner_name_label.place(x=20, y=100)
        self.winner_name_entry = Entry(master)
        self.winner_name_entry.place(x=100,y=100)

        self.surname_label = Label(master, text="Surname:")
        self.surname_label.place(x=20,y=150)
        self.surname_entry = Entry(master)
        self.surname_entry.place(x=100,y=150)

        self.emaiil_label = Label(master, text="email:")
        self.emaiil_label.place(x=20,y=200)
        self.email_entry = Entry(master)
        self.email_entry.place(x=100,y=200)

        self.amount_label = Label(master, text = "Amount:")
        self.amount_label.place(x=20,y=250)
        self.amount_entry = Entry(master)
        self.amount_entry.place(x=100,y=250)

        self.acount_label = Button(master, text = "Enter account number:", command = self.mail_check)
        self.acount_label.place(x=20,y=300)
        self.acount_entry = Entry(master)
        self.acount_entry.place(x=200,y=300)
        self.acount_entry.config(state = 'readonly')
        self.claim_btn = Button(master, text ="Claim", command = self.emailer)
        self.claim_btn.place(x=40, y=350)

        self.convert_btn = Button(master, text = "Convert to another currency.", command = self.convert_currency)
        self.convert_btn.place(x=200, y=350)

        self.exit_btn = Button(master, text = 'Exit')
        self.exit_btn.place(x= 250, y=400)
    # Function for checking the email.
    def mail_check(self):
        if "@" in self.email_entry.get():
            self.acount_entry.config(state='normal')

        else:
            messagebox.showinfo(title='Alert!', message="Please enter valid email adress!")
            self.acount_entry.config(state='readonly')
            self.email_entry.delete(0,END)

    # function to send the email and the winners information
    def emailer(self):
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        messagebox.showinfo(title="Submited", message="An email will be sent to you.")
        sender_email_id = 'stuurmanmzwandile@gmail.com'
        receiver_email_id = [self.email_entry.get()]
        password = "@strmzw001"
        subject = "Your winnings."
        msg = MIMEMultipart()
        msg['From'] = sender_email_id
        msg['To'] = ', ' .join(receiver_email_id)
        msg['Subject'] = subject
        body = "Your name:" + self.winner_name_entry.get() + "\n" + " " + "Your Surname:" + self.surname_entry.get() + "\n" + "Your Bank is:" + self.banks_list.get() + "\n" + "Your Account:" + self.acount_entry.get() + "\n" + "Amount: " + self.acount_entry.get()
        msg.attach(MIMEText(body, 'plain'))

        text = msg.as_string()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # start TLS for security
        s.starttls()
        # Authentication

        s.login(sender_email_id, password)
        # message to be sent

        # sending the mail
        s.sendmail(sender_email_id, receiver_email_id, text)
        # terminating the session
        s.quit()

        f = open("details.txt", "a") # appending all the information to a text file
        f.write("Acount holder: " + " " + self.winner_name_entry.get() + " " + self.surname_entry.get())
        f.write("Bank: " + self.banks_list.get() + "\n")
        f.write("Account number: " + self.acount_entry.get() + "\n")
        f.write("Amount:")
        root.destroy()
    def convert_currency(self):
        import currency_converter
        root.destroy()
    def exit(self):
        root.destroy()








y=Prize_claim(root)
root.mainloop()


