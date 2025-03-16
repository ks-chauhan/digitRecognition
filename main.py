from tkinter import *
from PIL import Image,ImageOps
import modelPrediction
from tkinter import Entry
def canvas_image():
    ps = canvas.postscript(file="drawing.ps", colormode='color')

    # Convert to an image using PIL
    img = Image.open("drawing.ps")
    img = ImageOps.crop(img, border=10)
    img = img.convert("L")  # Ensure proper color conversion
    img=img.resize((28,28))
    # Save as PNG or any other format
    img.save("drawing.png")
    global predicted_output
    predicted_output = modelPrediction.get_number(img)
    display_output(predicted_output)


def display_output(prediction):
    entry.config(state=NORMAL)
    entry.delete(0,END)
    entry.insert(0, prediction)
    entry.config(state=DISABLED)

def draw_start(event):
    global x_start, y_start
    x_start, y_start = event.x,event.y


def draw(event):
    global x_start, y_start
    x, y = event.x, event.y
    if ((x_start != None) and (y_start != None)):
        canvas.create_line(x_start, y_start, x, y, fill="white", smooth=True, width=30)
        canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="white", outline="white")

    x_start,y_start=event.x,event.y

def draw_end(event):
    global x_start, y_start
    x_start, y_start = None, None


def canvasClear():
    canvas.delete("all")
    canvas.create_rectangle(0, 0, 300, 300, fill="black", outline="black")

root = Tk()
root.title("Digit Recognition")
root.geometry("900x600")
topFrame = Frame(root)
topFrame.pack(side=TOP)
topLabel = Label(topFrame, text="Draw a Digit and check what the computer predicts")
topLabel.pack(side=TOP, fill=X, pady=30)
bottomFrame = Frame(root)
bottomFrame.pack(side=TOP,fill=X)
canvas = Canvas(bottomFrame, border=5, bg="black", height=300, width=300)
canvas.create_rectangle(0,0,300,300,fill="black", outline="black")
canvas.pack(side=LEFT, padx=50)
canvas.bind('<Button-1>', draw_start)
canvas.bind('<B1-Motion>', draw)
canvas.bind('<ButtonRelease-1>', draw_end)
bt=Button(bottomFrame, text="REDRAW", borderwidth=5,command=canvasClear)
bt.pack(side=LEFT)
bt=Button(bottomFrame, text="SUBMIT", borderwidth=5, command=canvas_image)
bt.pack(side=LEFT)
entry = Entry(bottomFrame, font=("Arial",50), width=1, state=DISABLED)
entry.pack(side=LEFT, padx=100)

root.mainloop()
