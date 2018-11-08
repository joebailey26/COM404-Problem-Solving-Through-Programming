from tkinter import *

class Gui(Tk):

    #initialises the Gui object
    def __init__(self):
        super().__init__()

        #set window attributes
        self.title("Newsletter")
        self.configure(height=250,
                       width=400)

        #add components
        self.add_heading_label()
        self.add_body_label()
        self.add_email_frame()
        self.add_email_label()
        self.add_entry()
        self.add_subscribe_button()

    def add_heading_label(self):
        #1. create the component
        self.heading_label = Label(pady=(12))
        self.heading_label.grid(row=0,column=0,columnspan=2)
        #2. style the component
        self.heading_label.configure(text="RECEIVE OUR NEWSLETTER",
                                     font="Arial 16")
        #3. assign events to the component

    def add_body_label(self):
        self.body_label = Label(pady=(12))
        self.body_label.grid(row=1,column=0,columnspan=2)
        self.body_label.configure(text="Please enter your email below to receive our newsletter.",
                                  font="Arial 10")

    def add_email_label(self):
        self.email_label = Label(self.email_frame)
        self.email_label.grid(row=3,column=0)
        self.email_label.configure(text="Email:",
                                   font="Arial 10")

    def add_entry(self):
        self.entry = Entry(self.email_frame)
        self.entry.grid(row=3,column=1)
        self.entry.configure(text="Subscribe",
                            width=40,
                            font="Arial 10")

    def add_subscribe_button(self):
        self.subscribe_button = Button()
        self.subscribe_button.grid(row=4,column=0,columnspan=2)
        self.subscribe_button.configure(text="Subscribe",
                                        width=45,
                                       font="Arial 10")

    def add_email_frame(self):
        self.email_frame = Frame(pady=(12))
        self.email_frame.grid()
