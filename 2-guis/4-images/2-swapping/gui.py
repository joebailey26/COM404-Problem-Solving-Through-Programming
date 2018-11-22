from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.cactus_image_2 = PhotoImage(file="cactus.gif")
        self.cactus_image = PhotoImage(file="cactus2.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_title_label()
        self.add_cactus_image_label()
        self.add_flip_button()

    def add_title_label(self):
        self.title_label = Label()
        self.title_label.grid(row=0, column=0)
        self.title_label.configure(text="Cactus Leaves",
                                   font="Arial 10")
        
    def add_cactus_image_label(self):
        self.cactus_image_label = Label()
        self.cactus_image_label.grid(row=1, column=0)
        self.cactus_image_label.configure(image=self.cactus_image,
                                             height=220,
                                             width=220)

    def add_flip_button(self):
        self.flip_button = Button()
        self.flip_button.grid(row=2, column=0)
        self.flip_button.configure(text="Submit",
                                   font="Arial 10")
        self.flip_button.bind("<ButtonRelease-1>", self.flip_button_clicked)
        
    def flip_button_clicked(self, event):
        self.cactus_image_label.configure(image=self.cactus_image_2,
                                             height=220,
                                             width=220)

                
        

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
