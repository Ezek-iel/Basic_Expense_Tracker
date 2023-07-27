from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame

def income_or_expense():
    if income.get() == 1:
        income_or_expense_check.config(bootstyle = "Success ToolButton", text = "Income")
    elif income.get() == -1:
        income_or_expense_check.config(bootstyle = "Danger ToolButton", text = "Expense")
    else:
        pass

def check_satisfied():
    if satisfied.get() == 1:
        satisfaction_check.config(bootstyle = "Success Round-Toggle", text = "Satisfied")
    elif satisfied.get() == 0:
        satisfaction_check.config(bootstyle = "Danger Round-Toggle", text = "Unsatisfied")

root = tb.Window(themename="darkly")
root.title("Add Transaction")
root.geometry("500x500")

title_label = tb.Label(root, text = "Add Transaction",font = ("Nunito",16))
title_label.grid(row = 0, column = 1, pady = 20, padx = 10)

income = IntVar()
satisfied = IntVar()

amount_entry_label = tb.Label(root, text = "Amount : ",font = ("Nunito",14))
amount_entry_label.grid(row = 1, column = 0, pady = 25, padx = 10)

amount_entry_entry = tb.Entry(root,font = ("Nunito",14))
amount_entry_entry.grid(row = 1, column = 1, pady = 25, padx = 10)

income_or_expense_label = tb.Label(root, text = "Income or Expense :",font = ("Nunito",14))
income_or_expense_label.grid(row = 2, column = 0, pady = 25, padx = 10)

income_or_expense_check = tb.Checkbutton(root, text = "Expense",bootstyle = "Info, Toolbutton", 
                                    width = 25,
                                    variable=income,
                                    onvalue=1,
                                    offvalue=-1,
                                    command = income_or_expense)
income_or_expense_check.grid(row = 2, column = 1,pady = 25, padx = 10)

satisfaction_label = tb.Label(root, text = "Satisfied? :",font = ("Nunito",14))
satisfaction_label.grid(row = 3, column = 0, pady = 25, padx = 10)

satisfaction_check = tb.Checkbutton(root, text = "Unsatisfied",bootstyle = "Info, Round-Toggle", width = 25,
                                    variable=satisfied,
                                    onvalue=1,
                                    offvalue=0,
                                    command = check_satisfied)
satisfaction_check.grid(row = 3, column = 1,pady = 25, padx = 10)

submit_button = tb.Button(root, text = "Submit")
submit_button.grid(row = 4, column = 1)


root.mainloop()