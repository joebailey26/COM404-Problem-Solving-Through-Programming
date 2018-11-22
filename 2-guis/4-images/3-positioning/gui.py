from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.map_image = PhotoImage(file="map.gif")
        self.bus_image = PhotoImage(file="bus.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_title_label()
        self.add_map_frame()
        self.add_map_image_label()
        self.add_bus_image_label()

    def add_title_label(self):
        self.title_label = Label()
        self.title_label.configure(text="Bus Journey",
                                   font="Arial 10")
        self.title_label.pack()

    def add_map_frame(self):
        self.map_frame = Frame()
        self.map_frame.configure(width=600, height=400)
        self.map_frame.pack()
        
    def add_map_image_label(self):    
        self.map_image_label = Label(self.map_frame)
        self.map_image_label.place(x=0, y=0)
        self.map_image_label.configure(image=self.map_image)
        
    def add_bus_image_label(self):
        self.bus_image_label = Label(self.map_frame)
        self.bus_image_label.place(x=10, y=10)
        self.bus_image_label.configure(image=self.bus_image)
        self.bus_image_label.bind("<B1-Motion>", self.add_bus_move)

    def add_bus_move(self, event):
        self.bus_image_label.place(x=event.x, y=event.y)

#Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
