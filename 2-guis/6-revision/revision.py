from tkinter import *

class Gui(Tk):

    #initialises the Gui object
    def __init__(self):
        super().__init__()

        # load resources
        self.loading_image = PhotoImage(file="loading.gif")
        self.filled_image = PhotoImage(file="filled.gif")
        self.empty_image = PhotoImage(file="empty.gif")
        
        #set window attributes
        self.title("Newsletter")
        self.configure(background='#eee',
                       padx=10,
                       pady=10,
                       width=400,
                       height=250,)

        #add components
        self.add_global_frame()
        
        self.add_heading_label()
        self.add_body_label()
        
        self.add_email_frame()
        self.add_email_label()
        self.add_loading_image_label()
        self.add_entry()
        
        self.add_type_frame()
        self.add_type_label()
        self.add_type_options()
        
        self.add_subscribe_button()
        self.add_animation_button()

    def add_heading_label(self):
        #1. create the component
        self.heading_label = Label(self.global_frame,pady=10)
        self.heading_label.grid(row=0,
                                column=0)
        #2. style the component
        self.heading_label.configure(text="RECEIVE OUR NEWSLETTER",
                                     font="Arial 14")
        #3. assign events to the component

    def add_body_label(self):
        self.body_label = Label(self.global_frame,anchor="w",padx=10,pady=10)
        self.body_label.grid(row=1,
                             column=0)
        self.body_label.configure(text="Please enter your email below to receive our newsletter.",
                                  font="Arial 10")

    def add_email_label(self):
        self.email_label = Label(self.email_frame,padx=10)
        self.email_label.grid(row=0,column=0)
        self.email_label.configure(text="Email:",
                                   font="Arial 10")
        
    def add_entry(self):
        self.entry = Entry(self.email_frame)
        self.entry.grid(row=0,column=1)
        self.entry.configure(text="Subscribe",
                             font="Arial 10",
                             border=2,
                             width=30,
                             fg="#f00")
        self.entry.bind("<KeyRelease>", self.check_entry)

    def check_entry(self, event):
        name = self.entry.get()
        if (name == ""):
            self.loading_image_label.configure(image=self.empty_image)
        else:
            self.loading_image_label.configure(image=self.filled_image)

    def add_loading_image_label(self):
        self.loading_image_label = Label(self.email_frame,padx=10)
        self.loading_image_label.grid(row=0, column=2)
        self.loading_image_label.configure(image=self.loading_image,
                                             height=20,
                                             width=20)

    def add_type_label(self):
        self.type_label = Label(self.type_frame,padx=10)
        self.type_label.grid(row=0,column=0)
        self.type_label.configure(text="Type",
                                   font="Arial 10")

    def add_type_options(self):
        self.choices = ["Weekly","Monthly","Yearly"]
        self.choices_selected = StringVar()
        self.choices_selected.set("Weekly")
        
        self.type_options = OptionMenu(self.type_frame, self.choices_selected, *self.choices)
        self.type_options.grid(row=0,column=1)
        self.type_options.configure(text="Type",
                                   font="Arial 10",width=30)
        
    def add_subscribe_button(self):
        self.subscribe_button = Button(self.global_frame)
        self.subscribe_button.grid(row=5,column=0)
        self.subscribe_button.configure(text="Subscribe",
                                       font="Arial 10",
                                        background='#fee',
                                        width=45)
        self.subscribe_button.bind("<ButtonRelease-1>", self.subscribe_button_clicked)

    def subscribe_button_clicked(self, event):
        name = self.entry.get()
        option = self.choices_selected.get()
        if (name == ""):
            messagebox.showinfo("Newsletter", "Please enter your email!")
        elif (option == "Weekly"):
            messagebox.showinfo("Newsletter", "You have subscribed to the weekly newsletter! You will receive this every Monday.")
        elif (option == "Monthly"):
            messagebox.showinfo("Newsletter", "You have subscribed to the monthly newsletter! You will receive this on the first day of every month.")
        elif (option == "Yearly"):
            messagebox.showinfo("Newsletter", "You have subscribed to the yearly newsletter! You will receive this at the start of each year.")    
        else:
            pass

    def add_animation_button(self):
        self.state = 0
        self.animation_button = Button(self.global_frame)
        self.animation_button.grid(row=6,column=0)
        self.animation_button.configure(text="Start Animation",
                                       font="Arial 10",
                                        background='#fee',
                                        width=45)
        self.animation_button.bind("<ButtonRelease-1>", self.animation_button_clicked)

    def animation_button_clicked(self, event):
        if (self.state==0):
            self.state = 1
            self.animation_button.configure(text="Stop Animation")
        else:
            self.state = 0
            self.animation_button.configure(text="Start Animation")
        
        self.animation_button.configure(text="Stop Animation")
    
    def add_email_frame(self):
        self.email_frame = Frame(self.global_frame,pady=10)
        self.email_frame.grid(row=3, column=0)

    def add_type_frame(self):
        self.type_frame = Frame(self.global_frame,pady=10)
        self.type_frame.grid(row=4, column=0)
        
    def add_global_frame(self):
        self.global_frame = Frame()
        self.global_frame.pack()
        
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
