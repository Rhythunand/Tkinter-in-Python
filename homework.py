import random
from tkinter import Tk, Label, Button, Frame, Text, Entry
import string

def generator() :
  password = ""
  number = int(input("Enter the number of characters for your password"))
  for i in range(number) :
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    password.append(lower)
    password.append(upper)
    passw = "".join(str(x)for x in password)
    label.config(text = passw)

root = Tk()
label = Label(root,font = ('arial',20,'bold'))
label.pack()
button = Button(root,text = 'Generate',command='gen')
root.geometry('500x500')
root.title('Password Generator')
root.mainloop()