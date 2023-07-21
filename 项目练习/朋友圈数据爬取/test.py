import tkinter as tk

def button_click():
    name = entry.get()
    label.config(text="Hello, " + name + "!")

window = tk.Tk()
window.title("My First Tkinter App")
window.geometry("400x300")

label = tk.Label(window, text="Hello, Tkinter!")
label.pack()

button = tk.Button(window, text="Click Me!", command=button_click)
button.pack()

entry = tk.Entry(window)
entry.pack()

window.mainloop()
