import sys
from tkinter import *
import tkinter.messagebox
from menu import Menu

class Login():
    def __init__(self,master):
        self.master = master
        # master is the frame or whole interface. Frame is the section of the whole screen you've chosen
        self.master = Frame(master, width=500, height=500,bg='#ffffff')
        self.master.pack()
        # administrator text
        self.heading = Label(self.master,text="ADMINISTRATOR",font=('arial 35 bold'),fg='black',bg='#ffffff')
        self.heading.place(x=55,y=0)
        # sign in to get access text
        self.access = Label(self.master,text="Please Sign In to get access",font=('arial 20'),fg='black',bg='#ffffff')
        self.access.place(x=80,y=50)
        # UserId label
        self.user_ID = Label(self.master,text="User ID: ",font=('arial 14'),fg="black",bg="#ffffff")
        self.user_ID.place(x=40,y=223)
        # Password label
        self.password = Label(self.master,text="Password: ",font=('arial 14'),fg="black",bg="#ffffff")
        self.password.place(x=40,y=263)
        # UserId entry box
        self.user_ID_ent = Entry(self.master,width=40)
        self.user_ID_ent.place(x=150,y=228)
        # Password entry box
        self.password_ent = Entry(self.master,width=40)
        self.password_ent.place(x=150,y=268)
        # gives user the user id and password
        # userid answer
        self.user_ans = Label(self.master,text="UserID: admin",bg='white')
        self.user_ans.place(x=40,y=423)
        # password answer
        self.pass_ans = Label(self.master,text="Password: admin",bg='white')
        self.pass_ans.place(x=40,y=453)
        # login button *** no cmd yet! ***
        self.login = Button(self.master, text="Login", width=33, bg='#b3b3ff', command=self.login_validation)
        self.login.place(x=153, y=303)
    def login_validation(self):
        if (self.user_ID_ent.get() == 'admin') and (self.password_ent.get() == 'admin'):  # go to menu
            print('success!')
            # destroying all previous Tkinter data in order to create an entirely new layout
            # opens main menu()
            master = Menu()
            my_menu = Menu(self.master)
        else:
            tkinter.messagebox.showinfo("Invalid Credentials", "Answers are in menu")

# store Tk() in root object. Root is a blank window!
root = Tk() # the window!
# store b as an instance of root
b = Login(root)
# size of root
root.geometry("500x500+0+0")
# cant be resized
root.resizable(False, False)
# just says that i will put your window in an infinite loop until you
# close the window yourself
root.mainloop()
