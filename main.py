from tkinter import *

window = Tk()
window.title("Pizarra")

canvas = Canvas(window, width=800, height=600, bg='black')
canvas.pack()

is_drawing = False
last_x, last_y = 0, 0
lines = []

def start_drawing(event):
    global is_drawing, last_x, last_y
    is_drawing = True
    last_x, last_y = event.x, event.y
canvas.bind('<Button-1>', start_drawing)

def stop_drawing(event):
    global is_drawing
    is_drawing = False
canvas.bind('<ButtonRelease-1>', stop_drawing)

def draw(event):
    global last_x, last_y
    if is_drawing:
        line = canvas.create_line(last_x, last_y, event.x, event.y, fill='white')
        lines.append(line)
        last_x, last_y = event.x, event.y
canvas.bind('<B1-Motion>', draw)

def undo(event):
    if lines:
        canvas.delete(lines.pop())
window.bind('<Control-z>', undo)

window.mainloop()