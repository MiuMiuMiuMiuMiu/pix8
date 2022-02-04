from tkinter import *
from tkinter import colorchooser

color_list = ["black"]
current_color = "black" # variable to store hex-code of color. Default when opening the program is black

#Shortcuts
def keydown(e):
    if e.char == "e":
        erase()         #e = Erasor
    elif e.char == "c":
        choose_color()  #c = Choose color
    elif e.char == "b":
        brush()         #b = Brush
    else:
        pass

def choose_color():
    '''Opens up colorpicker and assigns the hex-code for chosen color to the global variable "current_color" '''
    global color_list 
    global current_color
    color_code = colorchooser.askcolor(title ="Choose color")
    color_list.pop(0)
    color_list.insert(0, color_code[1])
    current_color = color_list[0]

def paint(event):
    '''Paints a square when clicked on'''
    global current_color
    #print('Got object click', event.x, event.y)
    #print(event.widget.find_closest(event.x, event.y))
    canvas.itemconfig(event.widget.find_closest(event.x, event.y), fill=current_color)

def brush():
    '''Assigns the global variable "current color" to user's chosen color'''
    global color_list 
    global current_color
    current_color = color_list[0]
    
def erase():
    '''Assigns global variable "current color" to white'''
    global current_color
    current_color = "white"

tk = Tk()
tk.title("Pix8")
tk.resizable(0, 0) #Fixed size, cannot be changed
canvas = Canvas(tk, width=600, height=500)
canvas.pack()
canvas.focus_set()

#Shortcuts
canvas.bind("<KeyPress>", keydown)

#Buttons
colorpicker = Button(tk, text= "Select color", command=choose_color)
eraser = Button(tk, text= "Eraser", command=erase)
paint_brush = Button(tk, text= "Brush", command=brush)

colorpicker.pack()
eraser.pack()
paint_brush.pack

colorpicker.place(x=15, y=50)
eraser.place(x=25, y=85)
paint_brush.place(x=25, y=115)

#Create 64 squares
for x in range(1, 65):
    canvas.create_rectangle(0, 0, 50, 50, fill="white", outline="grey", tags="pixel")

#Assign mouse click to squares and their corresponding function
canvas.tag_bind("pixel", '<ButtonPress-1>', paint)
canvas.tag_bind("pixel", '<B1-Motion>', paint)

#Arrange squares in 8x8 grid
i = 0 #Used to loop through while-loop
nr1 = 1 #starting range number, ex: 1
nr2 = 9 #starting range number, ex: 9
y = 100 #Position of Grid
while i in range(0,8):
    i = i + 1
    x = 0
    for pixel in range(nr1, nr2): #Repeat this code for the duration of while-loop (8 times)
        x = x + 50
        canvas.move(pixel, y, x)
    nr1 = nr2
    nr2 = nr2 + 8
    x = x + 50
    y = y + 50

tk.mainloop()