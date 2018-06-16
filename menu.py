#!/usr/bin/env python3

import tkinter as tk

class Menu(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, width=500, height=500, bg='#ffffff', **kwargs)
        # after these lines, it becomes a blank slate once again
        # title header
        self.clinic_header = tk.Label(self, text="+ Stephen's Clinic +", font=('arial 30'), fg='red', bg='white')
        self.clinic_header.place(x=80, y=0)
        # new patient button *** add cmd ***
        self.new_patient = tk.Button(self, text="Add a new patient", width=40, height=5, bg="#9999ff",command=self.add_patient)
        self.new_patient.place(x=105, y=130)
        # update patient button *** add cmd ***
        self.update_patient = tk.Button(self, text="Update/Delete Patients", width=40, height=5, bg="#9999ff",command=self.change_patient)
        self.update_patient.place(x=105, y=250)
        # schedule patient button *** add cmd ***
        self.schedule_patient = tk.Button(self, text="View Schedule", width=40, height=5, bg="#9999ff",command=self.view_schedule)
        self.schedule_patient.place(x=105, y=370)
    def add_patient(self):
            pass
    def change_patient(self):
            pass
    def view_schedule(self):
            pass

def main():
    """this is just for debugging, the normal entry point is in Login.py"""
    root = tk.Tk()
    # size of root
    b = Menu(root)
    b.pack()
    root.geometry("500x500+0+0")
    # cant be resized
    root.resizable(False, False)
    # just says that i will put your window in an infinite loop until you
    # close the window yourself
    root.mainloop()

if __name__ == "__main__":
    main()
