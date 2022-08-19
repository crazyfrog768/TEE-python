import tkinter as tk

def set_message():
    temptext = text_input.get()
    title_label.configure(text=temptext)

window=tk.Tk()
window.title('pyhon ')
window.minsize(width = 400, height=400)

title_label = tk.Label(master=window, text= 'hello title label')
title_label.pack()

text_input = tk.Entry(master=window)
text_input.pack()

ok_button = tk.Button(master=window, text='press for action', command=set_message)
ok_button.pack()

window.mainloop()

