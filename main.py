from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from date_time import current_date,current_time
from database_actions import show_all_records,delete_last_record,delete_all_records
import os
from ttkbootstrap.dialogs import Messagebox



# define all functions here

def request():
    """ The request function is called by the add_expense button and opens the ui_request file"""
    os.startfile("ui_request.py")

    
def refresh():
    """ This restarts the program hereby updating the views from the database"""
    os.startfile("main.py")
    quit()

def help():
    """Opens the help file associated with this program"""
    os.startfile("help.txt")

def delete_last():
    """This deletes the last record in the expense tracker file"""
    delete_last_record()
    mb = Messagebox.show_info("Last Record Deleted")
    if mb == None:
        """This restarts the program to update the views from the database"""
        os.startfile("main.py")
        quit()

def delete_all():
    mb = Messagebox.yesno(message = "Are you sure you want to delete all records?")
    if mb == "Yes":
        delete_all_records()
        os.startfile("main.py")
        quit()
    else:
        pass
    
        

# create all widgets here
root = tb.Window(themename = "darkly")
root.geometry("1000x720")
root.title("Expense Tracker")
root.iconbitmap("icon.ico")

# The title shows the title of the program and the current date
title_frame = tb.Frame(root)
title_frame.pack(pady = 15)

title_label = tb.Label(title_frame, text = "EZEKIEL's EXPENSE TRACKER", font = ("Nunito",18,"bold"))
title_label.grid(row = 0, column = 0, pady = 15, padx = 20)

date_label = tb.Label(title_frame, text = current_date, font = ("Nunito",12,UNDERLINE))
date_label.grid(row = 0, column = 1, pady = 15, padx =125)

# ----------------------------------------------------------------



def show_all_transactions():
    """ A function to show all transactions inside a scroll frame"""
    
    expense_data_frame = ScrolledFrame(root, width=900, height=550)  # The scrolled frame to show data inside
    expense_data_frame.pack()
    
    
    global transaction_frame  # Transaction records action frame
    transaction_frame = tb.Frame(root)
    transaction_frame.pack(pady = 10)

    global transaction_list # The list containing all the records from the database
    transaction_list = show_all_records()
    
    
    transaction_amount : list = [] # A list conatining all the amount used in the transaction to be calculated later
    
    for transaction in transaction_list:   # Loop through the records of the database
        
        # A frame containing all the Indivuidual Transactions
        expense_frame = tb.Frame(expense_data_frame, bootstyle = "dark")
        expense_frame.pack(pady = 25)
        #--------------------------------------------------------

        # A date time Frame containing the record of the date and time of the transaction
        expense_frame_date_time_frame = tb.Frame(expense_frame)
        expense_frame_date_time_frame.grid(row = 0, column = 0, pady = 10, padx = 20)
        
        # Date Label
        expense_frame_date_label = tb.Label(expense_frame_date_time_frame,text = transaction[0], font = ("Nunito",8))
        expense_frame_date_label.grid(row = 0,column = 0, pady = 10, padx = 20)

        date_seperator = tb.Separator(expense_frame_date_time_frame, orient = "horizontal")
        date_seperator.grid(row = 1, column = 0)
        
        # Time Label
        expense_frame_time_label = tb.Label(expense_frame_date_time_frame,text = transaction[1], font = ("Nunito",8))
        expense_frame_time_label.grid(row = 2,column = 0, pady = 10, padx = 20)

        sep1 = tb.Separator(expense_frame, orient = "vertical")
        sep1.grid(row = 0, column = 1, pady = 10)
        #---------------------------------------------------------------------------------------
        
        # Description Label containing the description of the expense
        expense_frame_description_label = tb.Label(expense_frame, text = transaction[2],font = ("Nunito",10), bootstyle = "Info Inverse")
        expense_frame_description_label.grid(row = 0, column = 2, pady = 10, padx = 20)

        sep2 = tb.Separator(expense_frame, orient = "vertical")
        sep2.grid(row = 0, column = 3, pady = 10)
        # -----------------------------------------------------------------------------------------

        # Amount Label containing the amount
        if transaction[4] == 1:
            # If amount was an income (gain)
            expense_frame_amount_label = tb.Label(expense_frame, text = (str(transaction[3]) + "$"),font = ("Nunito",10), bootstyle = "Success Inverse")
            expense_frame_amount_label.grid(row = 0, column = 4, pady = 10, padx = 20)
            
            # Append the current amount to the transaction list
            transaction_amount.append(transaction[3] * 1)
        elif transaction[4] == -1:
            # If amount was an expense (loss)
            expense_frame_amount_label = tb.Label(expense_frame, text = (str(transaction[3]) + "$"),font = ("Nunito",10), bootstyle = "Danger Inverse")
            expense_frame_amount_label.grid(row = 0, column = 4, pady = 10, padx = 20)

            # Append the current amount to the transaction list
            transaction_amount.append(transaction[3] * -1)

        sep3 = tb.Separator(expense_frame, orient = "vertical")
        sep3.grid(row = 0, column = 5, pady = 10)
        # --------------------------------------------------------------------------------------

        # Satisfaction label containing if user was satisfied or not
        if transaction[5] == 0:
            # If user was satisfied with the transaction he made
            expense_frame_satisfactory_label = tb.Label(expense_frame, text = "Not Satisfied",font = ("Nunito",10), bootstyle = "Danger Inverse")
            expense_frame_satisfactory_label.grid(row = 0, column = 6, pady = 10, padx = 20)
        elif transaction[5] == 1:
            # If user was not satisfied with the transaction he made
            expense_frame_satisfactory_label = tb.Label(expense_frame, text = "Satisfied",font = ("Nunito",10), bootstyle = "Success Inverse")
            expense_frame_satisfactory_label.grid(row = 0, column = 6, pady = 10, padx = 20)

    amount = sum(transaction_amount)  # Sum all the transactions  
    return amount # Return the current amount

show_all_transactions() # Call the functions


# Button to add expense to the Transaction list calling the request function
add_expense_button = tb.Button(transaction_frame, text = "Add Expense", bootstyle = "info", command = request)
add_expense_button.grid(column = 0, row = 0, padx = 10)
# -------------------------------------------------------------------------

# Button to refresh the whole program and again get information from the database
refresh_button = tb.Button(transaction_frame, text = "Refresh", bootstyle = "info", command = refresh)
refresh_button.grid(column = 1, row = 0, padx = 5)
# -------------------------------------------------------------------------


# Button when user needs to ask for help
help_button = tb.Button(transaction_frame, text = "Help", bootstyle = "info", command = help)
help_button.grid(column = 2, row = 0, padx = 5)
# -------------------------------------------------------------------------

# Button to delete last record
delete_last_button = tb.Button(transaction_frame, text = "Delete Last", bootstyle = "info", command = delete_last)
delete_last_button.grid(column = 3, row = 0, padx = 5)
# -------------------------------------------------------------------------

# Button to delete all records
delete_all_button = tb.Button(transaction_frame, text = "Delete All", bootstyle = "info", command = delete_all)
delete_all_button.grid(column = 4, row = 0, padx = 5)
# -------------------------------------------------------------------------

# Label showing the current amount available
current_amount_label = tb.Label(transaction_frame, text = "Current Amount :-> {0}  Dollars".format(show_all_transactions()),font = ("Nunito",13))
current_amount_label.grid(column = 5, row = 0, padx = 60)
# -------------------------------------------------------------------------

root.mainloop()