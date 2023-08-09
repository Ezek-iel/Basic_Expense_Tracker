from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame


# Window Configurations
root = tb.Window(themename = "darkly")
root.geometry("1000x720")
root.title("Expense Tracker")

# Creating the title frame
title_frame = tb.Frame(root)
title_frame.pack(pady = 15)

title_label = tb.Label(title_frame, text = "Expense Tracker", font = ("Nunito",18))
title_label.grid(row = 0, column = 0, pady = 15, padx = 20)

date_label = tb.Label(title_frame, text = "20 September 2023", font = ("Nunito",12,UNDERLINE))
date_label.grid(row = 0, column = 1, pady = 15, padx =125)

# Creating the expense data frame
expense_data_frame = ScrolledFrame(root, width=900, height=550)
expense_data_frame.pack()

for i in range(20):
    expense_frame = tb.Frame(expense_data_frame, bootstyle = "dark")
    expense_frame.pack(pady = 25)

    # Creating the expense date time frame
    expense_frame_date_time_frame = tb.Frame(expense_frame)
    expense_frame_date_time_frame.grid(row = 0, column = 0, pady = 10, padx = 20)

    expense_frame_date_label = tb.Label(expense_frame_date_time_frame,text = "23-09-34", font = ("Nunito",8))
    expense_frame_date_label.grid(row = 0,column = 0, pady = 10, padx = 20)

    date_seperator = tb.Separator(expense_frame_date_time_frame, orient = "horizontal")
    date_seperator.grid(row = 1, column = 0)

    expense_frame_time_label = tb.Label(expense_frame_date_time_frame,text = "14 : 45", font = ("Nunito",8))
    expense_frame_time_label.grid(row = 2,column = 0, pady = 10, padx = 20)

    sep1 = tb.Separator(expense_frame, orient = "vertical")
    sep1.grid(row = 0, column = 1, pady = 10)

    expense_frame_description_label = tb.Label(expense_frame, text = "Descripton Text",font = ("Nunito",10))
    expense_frame_description_label.grid(row = 0, column = 2, pady = 10, padx = 20)

    sep2 = tb.Separator(expense_frame, orient = "vertical")
    sep2.grid(row = 0, column = 3, pady = 10)

    expense_frame_amount_label = tb.Label(expense_frame, text = "3000",font = ("Nunito",10))
    expense_frame_amount_label.grid(row = 0, column = 4, pady = 10, padx = 20)

    sep3 = tb.Separator(expense_frame, orient = "vertical")
    sep3.grid(row = 0, column = 5, pady = 10)

    expense_frame_satisfactory_label = tb.Label(expense_frame, text = "Not Satisfactory",font = ("Nunito",10))
    expense_frame_satisfactory_label.grid(row = 0, column = 6, pady = 10, padx = 20)

transaction_frame = tb.Frame(root)
transaction_frame.pack(pady = 10)

add_expense_button = tb.Button(transaction_frame, text = "Add Expense", bootstyle = "info")
add_expense_button.grid(column = 0, row = 0, padx = 10)

refresh_button = tb.Button(transaction_frame, text = "Refresh", bootstyle = "info")
refresh_button.grid(column = 1, row = 0, padx = 5)

delete_last_button = tb.Button(transaction_frame, text = "Delete Last", bootstyle = "info")
delete_last_button.grid(column = 2, row = 0, padx = 5)

current_amount_label = tb.Label(transaction_frame, text = "Current Amount :-> ",font = ("Nunito",13))
current_amount_label.grid(column = 3, row = 0, padx = 45)



root.mainloop()