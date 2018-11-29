from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.ball_image = PhotoImage(file="ball.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.ball_x_pos = 0
        self.ball_y_pos = 225
        self.ball_x_change = 1
        
        # add components
        self.add_ball_image_label()
        self.add_up()
        self.add_down()
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        self.ball_x_pos = self.ball_x_pos + self.ball_x_change
        self.ball_image_label.place(x=self.ball_x_pos, 
                                    y=self.ball_y_pos)
        if self.ball_x_pos == 475:
            self.ball_x_change = -1
        elif self.ball_x_pos == 0:
            self.ball_x_change = 1
        else:
            pass

        self.after(10, self.tick)

    # the ball image
    def add_ball_image_label(self):
        self.ball_image_label = Label()
        self.ball_image_label.place(x=self.ball_x_pos,
                                    y=self.ball_y_pos)
        self.ball_image_label.configure(image=self.ball_image)

    def add_up(self):
        self.up = Button()
        self.up.place(x=150,
                      y=400)
        self.up.configure(text="Up")
        self.up.bind("<Button-1>", self.move_up)

    def move_up(self, event):
        self.ball_y_pos = self.ball_y_pos - 25

    def add_down(self):
        self.down = Button()
        self.down.place(x=250,
                      y=400)
        self.down.configure(text="Down")
        self.down.bind("<Button-1>", self.move_down)

    def move_down(self, event):
        self.ball_y_pos = self.ball_y_pos + 25
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 
