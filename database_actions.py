import sqlite3

# Sql files to be opened
sql_file = open("sql/add_record.sql","r").read()  
sql_file2 = open("sql/fetchall.sql","r").read()
sql_file3 = open("sql/delete_last_record.sql","r").read()
sql_file4 = open("sql/create_table.sql","r").read()

connection = sqlite3.connect("expense.db")   # Create a connection

cursor = connection.cursor() # Create a cursors

#cursor.execute(sql_file4)

connection.commit()

def add_record(date : str, time : str, description : str, amount : int, income_or_expense : int, satisfied : int) -> None:
    """To add a record to the table"""
    cursor.executemany(sql_file,[(date, time, description, amount, income_or_expense, satisfied)])
    connection.commit()


def show_all_records() -> list[tuple]:
    """Show all the records in a table"""
    cursor.execute(sql_file2)
    return cursor.fetchall()


def delete_last_record():
    """Delete the last record in a table"""
    record_length : int  = len(show_all_records())
    cursor.execute(sql_file3,str(record_length))
    connection.commit()

def delete_all_records():
    """Delete all the records in a table"""
    record_length : int = len(show_all_records())
    for i in range((record_length)):
        cursor.execute(sql_file3,str(i + 1))
    connection.commit()






