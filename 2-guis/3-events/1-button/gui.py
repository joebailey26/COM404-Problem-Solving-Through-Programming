from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_heading_label()
        self.add_instruction_label()
        self.add_tickets_entry()
        self.add_submit_button()
        
    def add_heading_label(self):
        #1. create the component
        self.heading_label = Label(pady=(12))
        self.heading_label.grid(row=0,column=0)
        #2. style the component
        self.heading_label.configure(text="Entrance Ticket",
                                     font="Arial 16")
        
    def add_instruction_label(self):
        #1. create the component
        self.instruction_label = Label(pady=(12))
        self.instruction_label.grid(row=1,column=0)
        #2. style the component
        self.instruction_label.configure(text="How many tickets are needed?",
                                     font="Arial 14")
        
    def add_tickets_entry(self):
        self.tickets_entry = Entry()
        self.tickets_entry.grid(row=2,column=0)
        self.tickets_entry.configure(width=40,)
        
    def add_submit_button(self):
        # create
        self.submit_button = Button()
        self.submit_button.grid(row=3, column=0)

        # style
        self.submit_button.configure(text="Submit")

        # events
        self.submit_button.bind("<ButtonRelease-1>", self.submit_button_clicked)
        
    def submit_button_clicked(self, event):
        tickets = self.tickets_entry.get()
        messagebox.showinfo("Purchased!", "You have purchased {} tickets!".format(tickets))
