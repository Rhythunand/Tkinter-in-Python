from tkinter import Tk, Label, Button, Frame, Text, Entry
window = Tk()
window.title('Tkinter Sample Window')
window.geometry('300x300')

greetings = Label(text = 'Hello User', fg = 'black', bg = 'white')
button = Button(text = 'Click Me', bg = 'black', fg = 'white')
entry = Entry(fg = 'yellow', bg = 'black', width = 50)
greetings.pack()
button.pack()
entry.pack()

frame = Frame(master = window, borderwidth = 5)
frame.pack()
label = Label(master = frame, text = 'Sample Frame')
label.pack()

textbox = Text(fg = 'green', bg = 'yellow')
textbox.pack()
window.mainloop()
