from tkinter import *

first_number = second_number = operator = None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def get_operator(op):
    global first_number, operator

    first_number = int(result_label['text'])
    operator = op
    result_label.config(text='')

def get_result():
    global first_number, second_number, operator

    second_number = int(result_label['text'])

    if operator == '+':
        result_label.config(text=str(first_number + second_number))
    elif operator == '-':
        result_label.config(text=str(first_number - second_number))
    elif operator == '*':
        result_label.config(text=str(first_number * second_number))
    else:
        if second_number == 0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(first_number / second_number, 2)))

root = Tk()
root.title('Calculator')
root.geometry('280x380')
root.configure(background='black')


for i in range(5):
    root.columnconfigure(i, weight=1)
for i in range(5):
    root.rowconfigure(i, weight=1)

result_label = Label(root, text='', bg='black', fg='white')
result_label.grid(row=0, column=0, columnspan=4, pady=(20, 20), sticky='nsew')
result_label.config(font=('verdana', 30, 'bold'))

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3),
]

for (text, row, col) in buttons:
    if text.isdigit() or text == 'C' or text == '=':
        bg = '#778899'
        cmd = lambda t=text: get_digit(t) if t.isdigit() else (clear() if t == 'C' else get_result())
    else:
        bg = '#FF8C00'
        cmd = lambda t=text: get_operator(t)
    
    button = Button(root, text=text, bg=bg, fg='white', command=cmd)
    button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
    button.config(font=('verdana', 14))

root.mainloop()
