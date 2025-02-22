import tkinter as tk

window = tk.Tk()

for i in range(3) :
  for x in range(3) :
    frame = tk.Frame(
      master = window,
      relief = tk.RAISED,
      borderwidth = 1
    )
    frame.grid(row=i, column=x, padx=5, pady = 5)
    label = tk.Label(master = frame, text = f"Row {i}\nColumn {x}")
    label.pack()

window.mainloop()