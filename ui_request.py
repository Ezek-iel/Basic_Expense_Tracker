from tkinter import *
from ttkbootstrap.constants import *
from date_time import *
import ttkbootstrap as tb
from ttkbootstrap.dialogs import Messagebox
import database_actions


def add_expense_ui():
    
    
    def get_data():
        """ Get the data from the submit button and send it to the record"""
        inc_or_exp : int= -1
        amount_str = amount_entry_entry.get()
        if amount_str.isnumeric() == True:
            amount = int(amount_str)
        else:
            warning_label.config(text = "Wrong Input", bootstyle = "Danger")
            mb = Messagebox.yesno(title = "Warning",message="This will record zero as the transaction amount \n Do you want this to happen", alert = True)
            if mb == "Yes":
                amount = 0
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
                pass
        else:
            if income.get() == 1:
                inc_or_exp = 1
            elif income.get() == -1:
                inc_or_exp = -1

            if satisfied.get() == 1:
                satisfied_  = 1
            elif satisfied.get() == 0:
                satisfied_  = 0
            database_actions.add_record(current_date,current_time,description_entry.get(),amount,inc_or_exp,satisfied_)
            mb = Messagebox.show_info("Expense Submitted","Succesful Input")
            if mb == None:
                quit()

            if mb == "No":
                pass
                    
        
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
    
    

    root = tb.Window(themename="darkly")
    root.title("Add Transaction")
    root.geometry("700x500")

    title_label = tb.Label(root, text = "Add Transaction",font = ("Nunito",16))
    title_label.grid(row = 0, column = 1, pady = 20, padx = 10)

    income = IntVar()
    satisfied = IntVar()

    # Entry to enter the amount
    amount_entry_label = tb.Label(root, text = "Amount : ",font = ("Nunito",14))
    amount_entry_label.grid(row = 1, column = 0, pady = 25, padx = 10)

    amount_entry_entry = tb.Entry(root,font = ("Nunito",14))
    amount_entry_entry.grid(row = 1, column = 1, pady = 25, padx = 10)
    # ---------------------------------------------------------------------------------

    # Entry to enter description
    description_label = tb.Label(root, text = "Description : ",font = ("Nunito",14))
    description_label.grid(row = 2, column = 0, pady = 25, padx = 10)

    description_entry = tb.Entry(root,font = ("Nunito",14))
    description_entry.grid(row = 2, column = 1, pady = 25, padx = 10)
    # ----------------------------------------------------------------------------------

    # Check to choose whether income or expense
    income_or_expense_label = tb.Label(root, text = "Income or Expense :",font = ("Nunito",14))
    income_or_expense_label.grid(row = 3, column = 0, pady = 25, padx = 10)

    income_or_expense_check = tb.Checkbutton(root, text = "Expense",bootstyle =  ("Toolbutton,Danger"), 
                                        width = 25,
                                        variable=income,
                                        onvalue=1,
                                        offvalue=-1,
                                        command = income_or_expense)
    income_or_expense_check.grid(row = 3, column = 1,pady = 25, padx = 10)
    #----------------------------------------------------------------------------------------

    # Check to choose wheter user was satisfied or not
    satisfaction_label = tb.Label(root, text = "Satisfied? :",font = ("Nunito",14))
    satisfaction_label.grid(row = 4, column = 0, pady = 25, padx = 10)

    satisfaction_check = tb.Checkbutton(root, text = "Unsatisfied",bootstyle = "Info Round-Toggle", width = 25,
                                        variable=satisfied,
                                        onvalue=1,
                                        offvalue=0,
                                        command = check_satisfied)
    satisfaction_check.grid(row = 4, column = 1,pady = 25, padx = 10)

    #---------------------------------------------------------------------------------

    # Button to submit calling the get_data function
    submit_button = tb.Button(root, text = "Submit",command = get_data, width = 35)
    submit_button.grid(row = 5, column = 1)
    # -------------------------------------------------------------------

    warning_label = tb.Label(root, text = " ", font = ("Nunito",14))
    warning_label.grid(row = 6, column = 1, pady = 10)


    root.mainloop()
add_expense_ui()