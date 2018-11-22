from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        # load resources
        self.name_tick_image = PhotoImage(file="tick.gif")
        self.name_cross_image = PhotoImage(file="cross.gif")
        self.pass_tick_image = PhotoImage(file="tick.gif")
        self.pass_cross_image = PhotoImage(file="cross.gif")
        self.nights_tick_image = PhotoImage(file="tick.gif")
        self.nights_cross_image = PhotoImage(file="cross.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_title_label()
        self.add_name_label()
        self.add_pass_label()
        self.add_nights_label()
        self.add_name_entry()
        self.add_pass_entry()
        self.add_nights_entry()
        self.add_name_image()
        self.add_pass_image()
        self.add_nights_image()
        self.add_check_button()

    def add_title_label(self):
        self.title_label = Label()
        self.title_label.configure(text="Hotel Check In",
                                   font="Arial 12")
        self.title_label.grid(row=0, column=0, columnspan=3)

    def add_name_label(self):
        self.name_label = Label()
        self.name_label.configure(text="Name:",
                                   font="Arial 10")
        self.name_label.grid(row=1, column=0)
        
    def add_pass_label(self):
        self.pass_label = Label()
        self.pass_label.configure(text="Passport Number:",
                                   font="Arial 10")
        self.pass_label.grid(row=2, column=0)

    def add_nights_label(self):
        self.nights_label = Label()
        self.nights_label.configure(text="No. of Nights:",
                                   font="Arial 10")
        self.nights_label.grid(row=3, column=0)

    def add_name_entry(self):
        self.name_entry = Entry()
        self.name_entry.grid(row=1, column=1)
        self.name_entry.bind("<FocusOut>", self.check_name_entry)
        
    def add_pass_entry(self):
        self.pass_entry = Entry()
        self.pass_entry.grid(row=2, column=1)
        self.pass_entry.bind("<FocusOut>", self.check_pass_entry)

    def add_nights_entry(self):
        self.nights_entry = Entry()
        self.nights_entry.grid(row=3, column=1)
        self.nights_entry.bind("<FocusOut>", self.check_nights_entry)

    def add_name_image(self):
        self.name_image = Label(self)
        self.name_image.grid(row=1, column=2)
        self.name_image.configure(image=self.name_cross_image)
        
    def add_pass_image(self):
        self.pass_image = Label(self)
        self.pass_image.grid(row=2, column=2)
        self.pass_image.configure(image=self.pass_cross_image)

    def add_nights_image(self):
        self.nights_image = Label(self)
        self.nights_image.grid(row=3, column=2)
        self.nights_image.configure(image=self.nights_cross_image)

    def add_check_button(self):
        self.check_button = Button()
        self.check_button.grid(row=4, column=0, columnspan=3)
        self.check_button.configure(text="Check In")

    def check_name_entry(self, event):
        name = self.name_entry.get()
        if (name == ""):
            self.name_image.configure(image=self.name_cross_image)
        else:
            self.name_image.configure(image=self.name_tick_image)

    def check_pass_entry(self, event):
        name = self.pass_entry.get()
        if (name == ""):
            self.pass_image.configure(image=self.pass_cross_image)
        else:
            self.pass_image.configure(image=self.pass_tick_image)

    def check_nights_entry(self, event):
        name = self.nights_entry.get()
        if (name == ""):
            self.nights_image.configure(image=self.nights_cross_image)
        else:
            self.nights_image.configure(image=self.nights_tick_image)
    

#Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
