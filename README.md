# Basic Expense Tracker
 A Basic Expense Tracker with ttkBootstrap and SQLite3

![main.py](/img/main.png)
> Preview Expenses

![ui_request.py](/img/add_expense.png)
> Add Expense

## How to Use.
 1. Open the [```main.py```](main.py)file to see the main code

 1. It has been updated to a notebook with 2 tabs, one for viewing transactions and one for adding transactions

 ![main.py](/img/notebook.png)

 > Using the Notebook Widget
 

## Things to Note.
 1. The transaction amount tab will be green for income (gaining money).

 1. The transaction amount tab will be red for expenses (spending money).

 1. The Satisfaction amount will be green if the user chooses to be satisfied with the transaction  made.

 1. The Satisfaction amount will be red if the user chooses to not be satisfied with the transaction  made.

 1. The total amount will be red (Danger) for balances that are less than 5000 and green for balances that are greater than 5000 *(5000 is the limit number)*

***You can contribute to the development of this simple GUI app, if you see an error please create a pull request and feel also free to clone this repository.***

> [TTKBootstrap](https://www.ttkbootstrap.readthedocs.io), [SQlite3](https://www.sqlite.com) and [auto_py_to_exe](https://pypi.org/project/auto-py-to-exe/) was used in this project.

TTkBootstrap can be installed via  
```python
pip install ttkbootstrap
```

auto_py_to_exe can be installed via
```python
pip install auto_py_to_exe
```
SQlite3 is pre-installed with python already

### **A stand-alone executable (***incase you dont want to go through the hassle of downloading libraries or you are a non programer***) is [Here](www.googledrive.com) (*87mb*)**

### Enjoy!!!

# For Developers
> The theme can be changed like a normal ttkbootstrap_theme 


> To get more info about ttkbootstrap_themes visit [the main website]("www.ttkbootstrap.io") or run
>```powershell
>python -m ttkbootstrap
>```
> in the command prompt or powershell


```python
# create all widgets here
root = tb.Window(themename = "solar") # Line 54
root.geometry("1000x720") # Line 55
root.title("Expense Tracker") # Line 56
# Line 53 to 56 of main.py
```

 > For point 5 in the [Things to Note section](#things-to-note), you could change the limit number here
 ```python
 # Label showing the current amount available
    if amount > 5000:
        # If amount is greater than 5000 show succesful amount
        current_amount_label = tb.Label(transaction_frame, text = "Current Amount :-> {0}  Naira".format(amount),font = ("Nunito",13), bootstyle = "Success")
        current_amount_label.grid(column = 5, row = 0, padx = 50)
        # -------------------------------------------------------------------------
    else:
        # show unsuccesful amount
        current_amount_label = tb.Label(transaction_frame, text = "Current Amount :-> {0}  Naira. Be Careful, Spend Wisely".format(amount),font = ("Nunito",13), bootstyle = "Warning")
        current_amount_label.grid(column = 5, row = 0, padx = 50)
        # -------------------------------------------------------------------------
 # Line 194 to Line 202 of main .py
 ```
>1. The app uses sqlite3 databasing. all databasing queries were wrapped in functions and
were called in the [```main.py```](main.py) file
>1. Those functions were written in the [```database_actions.py```](database_actions.py)

>The date and time were also wrapped in functions written in [```date_time.py```](date_time.py)

> The executable can be built using ```auto_py_to_exe``` and by calling 
>```powershell
>python -m auto_py_to_exe
>```
>in the command line or powershell
