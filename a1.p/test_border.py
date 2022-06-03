from curses import can_change_color
from tkinter import Canvas, Tk
from tkinter.constants import BOTH
from tkinter.ttk import Label
import time
import psutil
from psutil._common import BatteryTime
def move_window(event): # Moving the window
    root.geometry(f'+{event.x_root}+{event.y_root}')

def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs): # Creating a rounded rectangle
        
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True, fill="#1fa5fe")

root = Tk()
root.overrideredirect(1)
root.bind("<B1-Motion>", move_window)
root.eval('tk::PlaceWindow . center') # Placing the window in the center of the screen
root.title("Simple Battery and Clock App")
root.geometry('300x300')
root.config(background='grey')
root.attributes("-transparentcolor", "grey") # So that it doesn't look like a square

canvas = Canvas(root, bg="grey", highlightthickness=0)
canvas.pack(fill=BOTH, expand=1)

round_rectangle(0, 0, 300, 200, radius=70) # Creating the rounded rectangle/window

def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    day = time.strftime("%A")
    battery_data = psutil.sensors_battery()

    my_lab1.config(text='Battery {}% '.format(battery_data.percent))
    # if battery_data.power_plugged:
    #     mylab2.config(text="Plugged in")
    # else:
    #     mylab2.config(text="Not plugged")

    my_label.config(text=hour + ":" + minute)
    my_label.after(1000, clock)
    my_label2.config(text=day)

def update():

    my_label.config(text="New Text")

my_label = Label(canvas, text="", font=("Segoe UI Variable", 48), foreground='white', background='#1fa5fe')
my_label.pack(pady=20)

my_label2 = Label(canvas, text="", font=("Segoe UI Variable", 14), foreground='white', background='#1fa5fe')
my_label2.pack(pady=10)

my_lab1 = Label(canvas, text="", font=("Albertus", 14), foreground='white', background='#1fa5fe')
my_lab1.pack(pady=10)

# mylab2 = Label(canvas,text="",font=("Segeo UI Variable",10),foreground="white", background='#1fa5fe')
# mylab2.pack(pady=20)

clock()

root.mainloop()