from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.ball_image = PhotoImage(file="ball.gif")
        self.two_ball_image = PhotoImage(file="ball.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.ball_x_pos = 250
        self.ball_y_pos = 1
        self.ball_x_change = 1
        self.ball_y_change = 1
        self.two_ball_x_pos = 250
        self.two_ball_y_pos = 1
        self.two_ball_x_change = -1
        self.two_ball_y_change = -1
        
        # add components
        self.add_ball_image_label()
        self.add_two_ball_image_label()
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        self.ball_x_pos = self.ball_x_pos + self.ball_x_change
        self.ball_y_pos = self.ball_y_pos + self.ball_y_change
        self.ball_image_label.place(x=self.ball_x_pos, 
                                    y=self.ball_y_pos)
        if self.ball_x_pos == 475:
            self.ball_x_change = -1
        elif self.ball_y_pos == 475:
            self.ball_y_change = -1
        elif self.ball_x_pos == 0:
            self.ball_x_change = 1
        elif self.ball_y_pos == 0:
            self.ball_y_change = 1
        else:
            pass

        self.two_ball_x_pos = self.two_ball_x_pos + self.two_ball_x_change
        self.two_ball_y_pos = self.two_ball_y_pos + self.two_ball_y_change
        self.two_ball_image_label.place(x=self.two_ball_x_pos, 
                                    y=self.two_ball_y_pos)
        if self.two_ball_x_pos == 475:
            self.two_ball_x_change = -1
        elif self.two_ball_y_pos == 475:
            self.two_ball_y_change = -1
        elif self.two_ball_x_pos == 0:
            self.two_ball_x_change = 1
        elif self.two_ball_y_pos == 0:
            self.two_ball_y_change = 1
        else:
            pass
        
        self.after(10, self.tick)

    # the ball image
    def add_ball_image_label(self):
        self.ball_image_label = Label()
        self.ball_image_label.place(x=self.ball_x_pos,
                                    y=self.ball_y_pos)
        self.ball_image_label.configure(image=self.ball_image)

    def add_two_ball_image_label(self):
        self.two_ball_image_label = Label()
        self.two_ball_image_label.place(x=self.two_ball_x_pos,
                                    y=self.two_ball_y_pos)
        self.two_ball_image_label.configure(image=self.two_ball_image)
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 
