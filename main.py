# All imports here -> Tkinter, ttkbootstrap, indirectly: time and sqlite modules


from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import * 
from ttkbootstrap.scrolled import ScrolledFrame
from date_time import current_date,current_time
from database_actions import show_all_records,delete_last_record,delete_all_records,add_record
from ttkbootstrap.dialogs import Messagebox



# define all functions here

def request():
    """ The request function is called by the add_expense button and opens the ui_request file"""
    overall_notebook.select(overall_notebook.tabs()[1])

    
def refresh():
    """ This restarts the program hereby updating the views from the database"""
    load()

def help():
    """Opens the help file associated with this program"""
    help_mb = Messagebox.ok(message="""
        This is an expense tracker. you can add an expense by pressing the
        add expense button. you can also delete all expenses as 
        well 
""",
         title="Help Info"   )

def delete_last():
    """This deletes the last record in the expense tracker file"""
    
    mb = Messagebox.yesno(message = "Are you sure you want to delete the last record?")
    if mb == "Yes":
        delete_last_record()
        mb2 = Messagebox.show_info("Last Record Deleted")
        load()
    else:
        pass

def delete_all():
    """deletes all records in the database"""
    mb = Messagebox.yesno(message = "Are you sure you want to delete all records?")
    if mb == "Yes":
        delete_all_records()
        load()
    else:
        pass
    
        

# create all widgets here
root = tb.Window(themename = "solar")
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

overall_notebook = tb.Notebook(root)
overall_notebook.pack(pady = 10)

add_expense_tab = Frame(root)
view_expense_tab = Frame(root)
def load():
    """ The load function loads all the expenses"""
      
    view_scrolled_frame = ScrolledFrame(view_expense_tab, width = 900, height = 550)
    view_scrolled_frame.grid(row = 0, column = 0)
 
            
    expense_data_frame = ScrolledFrame(view_scrolled_frame, width=800, height=500, bootstyle = DARK)  # The scrolled frame to show data inside
    expense_data_frame.pack()
        
        
    global transaction_frame  # Transaction records action frame
    transaction_frame = tb.Frame(view_scrolled_frame)
    transaction_frame.pack(pady = 10)

    global transaction_list # The list containing all the records from the database
    transaction_list = show_all_records()
        
        
    transaction_amount : list = [] # A list conatining all the amount used in the transaction to be calculated later
        
    for transaction in transaction_list:   # Loop through the records of the database
            
        # A frame containing all the Indivuidual Transactions
        expense_frame = tb.Frame(expense_data_frame, bootstyle = "light")
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

    global amount
    amount = sum(transaction_amount)  # Sum all the transactions  
     # Return the current amount

     # Call the functions


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
    if amount > 5000:
        current_amount_label = tb.Label(transaction_frame, text = "Current Amount :-> {0}  Naira".format(amount),font = ("Nunito",13), bootstyle = "Success")
        current_amount_label.grid(column = 5, row = 0, padx = 50)
        # -------------------------------------------------------------------------
    else:
        current_amount_label = tb.Label(transaction_frame, text = "Current Amount :-> {0}  Naira. Be Careful, Spend Wisely".format(amount),font = ("Nunito",13), bootstyle = "Warning")
        current_amount_label.grid(column = 5, row = 0, padx = 50)
        # -------------------------------------------------------------------------

load()
#  UI of the second tab (Add Expense Tab)

def add_expense_ui():
    
    def clear_entry_data():
        """ This will clear all the entered entry data"""
        amount_entry_entry.delete(0,END)
        description_entry.delete(0,END)
    
    def get_data():
        """ Get the data from the submit button and send it to the record"""
        inc_or_exp : int= -1
        satisfied_ : int = 0
        amount_str = amount_entry_entry.get()
        if amount_str.isnumeric() == True:
            amount_recorded = int(amount_str)
        else:
            warning_label.config(text = "Wrong Input", bootstyle = "Danger")
            mb = Messagebox.yesno(title = "Warning",message="This will record zero as the transaction amount \n Do you want this to happen", alert = True)
            if mb == "Yes":
                warning_label.config(text = "")
                amount_recorded = 0
                if income.get() == 1:
                    inc_or_exp = 1
                elif income.get() == -1:
                    inc_or_exp = -1

                if satisfied.get() == 1:
                    satisfied_ += 1
                elif satisfied.get() == 0:
                    satisfied_ += 0
                
        if len(description_entry.get()) == 0:
            mb2 = Messagebox.show_warning(title = "Warning",message="No Description Text Available", alert = True)
            if mb2 == None:
                warning_label.config(text = "")
                pass
        else:
            if income.get() == 1:
                inc_or_exp = 1
            elif income.get() == -1:
                inc_or_exp = -1

            if satisfied.get() == 1:
                satisfied_  += 1
            elif satisfied.get() == 0:
                satisfied_  += 0
            add_record(current_date,current_time,description_entry.get(),amount_recorded,inc_or_exp,satisfied_)
            warning_label.config(text="")
            mb = Messagebox.show_info("Expense Submitted","Succesful Input")
            clear_entry_data()
            load()
            overall_notebook.select(overall_notebook.tabs()[0])
                    
        
    def income_or_expense():
        """Function to check if transaction was income (gain) or expense (loss)"""
        if income.get() == 1:
            income_or_expense_check.config(bootstyle = "Success ToolButton", text = "Income")
        elif income.get() == -1:
            income_or_expense_check.config(bootstyle = "Danger ToolButton", text = "Expense")
        else:
            pass

    def check_satisfied():
        """Function to check if user was satisfied with transaction or not"""
        if satisfied.get() == 1:
            satisfaction_check.config(bootstyle = "Success Round-Toggle", text = "Satisfied")
        elif satisfied.get() == 0:
            satisfaction_check.config(bootstyle = "Danger Round-Toggle", text = "Unsatisfied")
    
    

    
    title_label = tb.Label(add_expense_tab, text = "Add Transaction",font = ("Nunito",16))
    title_label.grid(row = 0, column = 1, pady = 20, padx = 10)

    income = IntVar()
    satisfied = IntVar()

    # Entry to enter the amount
    amount_entry_label = tb.Label(add_expense_tab, text = "Amount : ",font = ("Nunito",14))
    amount_entry_label.grid(row = 1, column = 0, pady = 25, padx = 10)

    amount_entry_entry = tb.Entry(add_expense_tab,font = ("Nunito",14))
    amount_entry_entry.grid(row = 1, column = 1, pady = 25, padx = 10)
    # ---------------------------------------------------------------------------------

    # Entry to enter description
    description_label = tb.Label(add_expense_tab, text = "Description : ",font = ("Nunito",14))
    description_label.grid(row = 2, column = 0, pady = 25, padx = 10)

    description_entry = tb.Entry(add_expense_tab,font = ("Nunito",14))
    description_entry.grid(row = 2, column = 1, pady = 25, padx = 10)
    # ----------------------------------------------------------------------------------

    # Check to choose whether income or expense
    income_or_expense_label = tb.Label(add_expense_tab, text = "Income or Expense :",font = ("Nunito",14))
    income_or_expense_label.grid(row = 3, column = 0, pady = 25, padx = 10)

    income_or_expense_check = tb.Checkbutton(add_expense_tab, text = "Expense",bootstyle =  ("Toolbutton,Danger"), 
                                        width = 25,
                                        variable=income,
                                        onvalue=1,
                                        offvalue=-1,
                                        command = income_or_expense)
    income_or_expense_check.grid(row = 3, column = 1,pady = 25, padx = 10)
    #----------------------------------------------------------------------------------------

    # Check to choose wheter user was satisfied or not
    satisfaction_label = tb.Label(add_expense_tab, text = "Satisfied? :",font = ("Nunito",14))
    satisfaction_label.grid(row = 4, column = 0, pady = 25, padx = 10)

    satisfaction_check = tb.Checkbutton(add_expense_tab, text = "Unsatisfied",bootstyle = "Info Round-Toggle", width = 25,
                                        variable=satisfied,
                                        onvalue=1,
                                        offvalue=0,
                                        command = check_satisfied)
    satisfaction_check.grid(row = 4, column = 1,pady = 25, padx = 10)

    #---------------------------------------------------------------------------------

    # Button to submit calling the get_data function
    submit_button = tb.Button(add_expense_tab, text = "Submit",command = get_data, width = 35)
    submit_button.grid(row = 5, column = 1)
    # -------------------------------------------------------------------

    warning_label = tb.Label(add_expense_tab, text = " ", font = ("Nunito",14))
    warning_label.grid(row = 6, column = 1, pady = 10)

    


    
add_expense_ui()


overall_notebook.add(view_expense_tab, text = "VIEW TRANSACTIONS")
overall_notebook.add(add_expense_tab,text = "ADD TRANSACTIONS")


root.mainloop()