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
        self.add_email_label()
        self.add_subscribe_button()
        self.add_entry()

    def add_heading_label(self):
        #1. create the component
        self.heading_label = Label()
        self.heading_label.place(x=55, y=25)
        #2. style the component
        self.heading_label.configure(text="RECEIVE OUR NEWSLETTER",
                                     font="Arial 16")
        #3. assign events to the component

    def add_body_label(self):
        self.body_label = Label()
        self.body_label.place(x=45, y=75)
        self.body_label.configure(text="Please enter your email below to receive our newsletter.",
                                  font="Arial 10")

    def add_email_label(self):
        self.email_label = Label()
        self.email_label.place(x=5, y=125)
        self.email_label.configure(text="Email:",
                                   font="Arial 10")

    def add_entry(self):
        self.entry = Entry()
        self.entry.place(x=50, y=125)
        self.entry.configure(text="Subscribe",
                            width=40,
                            font="Arial 10")

    def add_subscribe_button(self):
        self.subscribe_button = Button()
        self.subscribe_button.place(x=10, y=200)
        self.subscribe_button.configure(text="Subscribe",
                                        width=45,
                                       font="Arial 10")
