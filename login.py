#!/usr/bin/env python3

import tkinter as tk
import tkinter.messagebox
from menu import Menu

class Login(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, bg='#ffffff', **kwargs)
        self.columnconfigure(0, weight=1)

        # administrator text
        self.heading = tk.Label(self,text="ADMINISTRATOR",font=('arial 35 bold'),fg='black',bg='#ffffff')
        self.heading.grid()
        # sign in to get access text
        self.access = tk.Label(self,text="Please Sign In to get access",font=('arial 20'),fg='black',bg='#ffffff')
        self.access.grid()

        credentials = tk.Frame(self, bg='#ffffff')
        credentials.grid()
        self.rowconfigure(2, weight=1) # set this row to take up all available space
        # UserId label
        self.user_ID = tk.Label(credentials,text="User ID: ",font=('arial 14'),fg="black",bg="#ffffff")
        self.user_ID.grid(row=0, column=0)
        # Password label
        self.password = tk.Label(credentials,text="Password: ",font=('arial 14'),fg="black",bg="#ffffff")
        self.password.grid(row=1, column=0)
        # UserId entry box
        self.user_ID_ent = tk.Entry(credentials,width=40)
        self.user_ID_ent.grid(row=0, column=1)
        # Password entry box
        self.password_ent = tk.Entry(credentials,width=40)
        self.password_ent.grid(row=1, column=1)

        self.login = tk.Button(self, text="Login", width=33, bg='#b3b3ff', command=self.login_validation)
        self.login.grid()

        # gives user the user id and password
        # userid answer
        self.user_ans = tk.Label(self,text="UserID: admin",bg='white')
        self.user_ans.grid()
        # password answer
        self.pass_ans = tk.Label(self,text="Password: admin",bg='white')
        self.pass_ans.grid()
        # login button *** no cmd yet! ***

    def login_validation(self):
        if (self.user_ID_ent.get() == 'admin') and (self.password_ent.get() == 'admin'):  # go to menu
            print('success!')
            # destroying all previous Tkinter data in order to create an entirely new layout
            # opens main menu()
            master = Menu(self.master)
            master.pack()
            self.destroy()
        else:
            tkinter.messagebox.showinfo("Invalid Credentials", "Answers are in menu")

def main():
    # store Tk() in root object. Root is a blank window!
    root = tk.Tk() # the window!
    # store b as an instance of root
    b = Login(root)
    b.pack(fill=tk.BOTH, expand=True)
    # size of root
    root.geometry("500x500+0+0")
    # cant be resized
    root.resizable(False, False)
    # just says that i will put your window in an infinite loop until you
    # close the window yourself
    root.mainloop()

if __name__ == "__main__":
    main()

