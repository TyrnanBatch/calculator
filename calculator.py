import tkinter as tk
import re

root = tk.Tk()

calculation_input = ''

def calculator(calculation_input):
    result = re.split('(\W)', calculation_input)

    result_length = len(result)

    count = 0
    for char in range(result_length):
        if count >= len(result):
            continue
        if len(result) == 1:
            return result[0]
        if result[count] == '*':
            multiply_result = int(result[count-1]) * int(result[count+1])
            result[count] = multiply_result
            del result[count-1]
            del result[count]
            count = 0
        if result[count] == '/':
            divide_result = int(result[count-1]) / int(result[count+1])
            result[count] = divide_result
            del result[count-1]
            del result[count]
            count = 0
        count += 1

    count = 0
    for char in range(result_length):
        if len(result) == 1:
            return result[0]
        if result[count] == '+':
            plus_result = int(result[count-1]) + int(result[count+1])
            result[count] = plus_result
            del result[count-1]
            del result[count]
            count = 0
        if result[count] == '-':
            minus_result = int(result[count-1]) - int(result[count+1])
            result[count] = minus_result
            del result[count-1]
            del result[count]
            count = 0
        count += 1

def one_function():
    global calculation_input
    calculation_input += '1'
    calculation_text.set(calculation_input)
def two_function():
    global calculation_input
    calculation_input += '2'
    calculation_text.set(calculation_input)
def three_function():
    global calculation_input
    calculation_input += '3'
    calculation_text.set(calculation_input)
def four_function():
    global calculation_input
    calculation_input += '4'
    calculation_text.set(calculation_input)
def five_function():
    global calculation_input
    calculation_input += '5'
    calculation_text.set(calculation_input)
def six_function():
    global calculation_input
    calculation_input += '6'
    calculation_text.set(calculation_input)
def seven_function():
    global calculation_input
    calculation_input += '7'
    calculation_text.set(calculation_input)
def eight_function():
    global calculation_input
    calculation_input += '8'
    calculation_text.set(calculation_input)
def nine_function():
    global calculation_input
    calculation_input += '9'
    calculation_text.set(calculation_input)
def zero_function():
    global calculation_input
    calculation_input += '0'
    calculation_text.set(calculation_input)

def multiply_function():
    global calculation_input
    if calculation_input[-1] != '*' and calculation_input[-1] != '/' and calculation_input[-1] != '+' and calculation_input[-1] != '-':
        calculation_input += '*'
        calculation_text.set(calculation_input)
def divide_function():
    global calculation_input
    if calculation_input[-1] != '*' and calculation_input[-1] != '/' and calculation_input[-1] != '+' and calculation_input[-1] != '-':
        calculation_input += '/'
        calculation_text.set(calculation_input)
def add_function():
    global calculation_input
    if calculation_input[-1] != '*' and calculation_input[-1] != '/' and calculation_input[-1] != '+' and calculation_input[-1] != '-':
        calculation_input += '+'
        calculation_text.set(calculation_input)
def minus_function():
    global calculation_input
    if calculation_input[-1] != '*' and calculation_input[-1] != '/' and calculation_input[-1] != '+' and calculation_input[-1] != '-':
        calculation_input += '-'
        calculation_text.set(calculation_input)

def equal_function():
    global calculation_input
    calculation_text.set(calculator(calculation_input))
    calculation_input = ''
def del_function():
    global calculation_input
    calculation_input = calculation_input[:-1]
    calculation_text.set(calculation_input)
def clear_function():
    global calculation_input
    calculation_input = ''
    calculation_text.set(calculation_input)

calculation_text = tk.StringVar()
calculation_text.set('0')
calculation_input_label = tk.Label(root, textvariable=calculation_text, font='40')
calculation_input_label.grid(row=1, column=1, columnspan=5)

#keypad numbers
one_button = tk.Button(root, text='1', font='20', height=2, width=4, command=one_function)
one_button.grid(row=2, column=1)
two_button = tk.Button(root, text='2', font='20', height=2, width=4, command=two_function)
two_button.grid(row=2, column=2)
three_button = tk.Button(root, text='3', font='20', height=2, width=4, command=three_function)
three_button.grid(row=2, column=3)
four_button = tk.Button(root, text='4', font='20', height=2, width=4, command=four_function)
four_button.grid(row=3, column=1)
five_button = tk.Button(root, text='5', font='20', height=2, width=4, command=five_function)
five_button.grid(row=3, column=2)
six_button = tk.Button(root, text='6', font='20', height=2, width=4, command=six_function)
six_button.grid(row=3, column=3)
seven_button = tk.Button(root, text='7', font='20', height=2, width=4, command=seven_function)
seven_button.grid(row=4, column=1)
eight_button = tk.Button(root, text='8', font='20', height=2, width=4, command=eight_function)
eight_button.grid(row=4, column=2)
nine_button = tk.Button(root, text='9', font='20', height=2, width=4, command=nine_function)
nine_button.grid(row=4, column=3)
zero_button = tk.Button(root, text='0', font='20', height=2, width=4, padx=47, command=zero_function)
zero_button.grid(row=5, column=1, columnspan=3)
#keypad functions
multiply_button = tk.Button(root, text='x', font='20', height=2, width=4, command=multiply_function)
multiply_button.grid(row=2, column=4)
divide_button = tk.Button(root, text='/', font='20', height=2, width=4, command=divide_function)
divide_button.grid(row=2, column=5)
add_button = tk.Button(root, text='+', font='20', height=2, width=4, command=add_function)
add_button.grid(row=3, column=4)
minus_button = tk.Button(root, text='-', font='20', height=2, width=4, command=minus_function)
minus_button.grid(row=3, column=5)
equal_button = tk.Button(root, text='clear', font='20', height=2, width=4, command=clear_function)
equal_button.grid(row=4, column=5)
delete_button = tk.Button(root, text='del', font='20', height=2, width=4, command=del_function)
delete_button.grid(row=4, column=4)
clear_button = tk.Button(root, text='=', font='20', height=2, width=4, padx=24, command=equal_function)
clear_button.grid(row=5, column=4, columnspan=2)


root.mainloop()
