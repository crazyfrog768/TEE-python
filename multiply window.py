import tkinter as tk

def show_output():
    number = 0
    number = int(number)

    try:
        number = int(number_input.get())
        if number == 0:
            raise Exception()
    except:
        output_label.configure(text = 'this is wrong ...')
        return

    output = ''
    for i in range(1, 13, 1):
        output += str(number) + ' * ' + str(i)
        output += ' = ' + str(number*i) + '\n'
    output_label.configure(text=output)


window=tk.Tk()
window.title('สูตรคูณ')
window.minsize(width=400, height=400)

title_label=tk.Label(master=window, text='สูตรคูณ')
title_label.pack(pady=10)

number_input=tk.Entry(master=window,
                      width=15)
number_input.pack()

go_button=tk.Button(master=window, text='go for it'
                    , command=show_output,
                    width=15, height=1)
go_button.pack()

output_label=tk.Label(master=window)
output_label.pack()

window.mainloop()